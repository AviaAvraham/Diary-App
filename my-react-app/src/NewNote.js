import React, { useState } from 'react';
import axios from 'axios';
import './NewNote.css'; // Import your CSS file
import PromptArea from './PromptArea.js';

function NewNote() {
    const [message, setMessage] = useState("");

    const sendMessage = async () => {
        try {
            const response = await axios.post('http://localhost:5000/new', { message });
            //setMessageCount(response.data.message_count);
            setMessage("");
        } catch (error) {
            console.error("Error occurred:", error);
        }
    };

    return (
        <div>
            <PromptArea/>
            <div className="container">
                <div className="input-container">
                    <textarea
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        placeholder="Type your note here..."
                    />
                </div>
                <div className="button-container">
                    <button onClick={sendMessage}>Save Note</button>
                </div>
            </div>
        </div>
    );
}

export default NewNote;
