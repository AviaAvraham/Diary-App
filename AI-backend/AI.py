import json
from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List, Dict, Any

load_dotenv(override=True)


MODEL = "gpt-4-1106-preview"
PROMPT_INITIAL = ""
PROMPT_CONT = ""
with open("prompt_initial.txt", "r") as file:
    PROMPT_INITIAL = file.read()
with open("prompt_cont.txt", "r") as file:
    PROMPT_CONT = file.read()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


# Dict[str, Any] is basically the same as a JSON object
def load_conversation_history(patient_id:int) -> List[Dict[str, Any]]:
    filename = f"history.json"
    
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            json_file = json.load(file)
            try:
                return json_file[str(patient_id)]
            except KeyError:
                return [ 
                    {"role": "system", "content": "You are my cognitive-behavioral assitant in a digital diary therapy application. Your role is to encourage the patient to write in the diary, and help him process his thoughts and emotions."},
                    {"role": "system", "content": PROMPT_INITIAL}
                ]
        return []

def save_conversation_history(patient_id: int, current_conversation: List[Dict[str, Any]]) -> None:
    existing_history_patient = load_conversation_history(patient_id)
    existing_history_patient.append(current_conversation)
    conversation_history = {patient_id: existing_history_patient}
    filename = f"history.json"
    with open(filename, 'w') as file:
        json.dump(conversation_history, file)

def generate_response(patient_id: int) -> str:
    # Load conversation history from database or file
    conversation_history = load_conversation_history(patient_id)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=conversation_history
        )

        # Extract and return the assistant's reply
        assistant_reply = response.choices[0].message.content

        # Save the assistant's reply to the conversation history
        conversation_history.append({"role": "assistant", "content": assistant_reply})
        save_conversation_history(patient_id, conversation_history)

        return assistant_reply
    except Exception as e:
        return f"An error occurred: {e}"

def assign_patient_id() -> int:
    # backend logic
    return 0

def main():
    my_id = 216
    print("GPT-4 Response:", generate_response(my_id))
 

if __name__ == "__main__":
    main()
