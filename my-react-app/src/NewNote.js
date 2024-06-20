import React, { useState } from 'react';
import axios from 'axios';
import './NewNote.css'; // Import your CSS file

function NewNote() {
    const [message, setMessage] = useState("");
    const [messageCount, setMessageCount] = useState(0);

    const sendMessage = async () => {
        try {
            const response = await axios.post('http://localhost:5000/new', { message });
            setMessageCount(response.data.message_count);
            setMessage(""); // Clear the input after sending message
        } catch (error) {
            console.error("Error occurred:", error);
        }
    };

    return (
        <div className="container"><div className="input-container">
    </div>
            <div className="input-container">
                <textarea
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Type your note here..."
                />
            </div>
            <div className="button-container">
                <button onClick={sendMessage}>Send Note</button>
            </div>
        </div>
    );
}

export default NewNote;
