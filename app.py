from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS
from datetime import datetime
import sqlite3
from llm2 import upload_doc, generate_writing_prompt
import time

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Initialize database
def init_db():
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# @app.route('/')
# def index():
#     conn = sqlite3.connect('diary.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT id, date, content FROM notes ORDER BY date DESC')
#     notes = cursor.fetchall()
#     conn.close()
#     return render_template('index.html', notes=notes)

@app.route('/getNotes', methods=['GET'])
def get_notes():
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, date, content FROM notes ORDER BY date DESC')
    notes = cursor.fetchall()
    conn.close()
    
    def convert_bytes(item):
        if isinstance(item, bytes):
            return item.decode('utf-8')
        return item
    
    notes_serializable = [{'id': id, 'date': date, 'message': convert_bytes(message)} for id, date, message in notes]
    return jsonify(notes_serializable)

@app.route('/new', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        print(request.json["message"])
        content = request.json["message"]
        date = datetime.now().strftime('%Y-%m-%d')
        conn = sqlite3.connect('diary.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (date, content) VALUES (?, ?)', (date, content))
        conn.commit()
        conn.close()
        upload_doc(content, "123", f"{time.time}") # TODO change instead of 1

        return redirect(url_for('new_note')) # not sure what to return here
    return "wrong place!"


@app.route('/prompt')
def get_prompt():
    prompt = generate_writing_prompt("123") # TODO change id here too
    #prompt = "Disabled for now"
    print(prompt)
    print(jsonify({'prompt': prompt}))
    return jsonify({'prompt': prompt})
    


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
