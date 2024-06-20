import React, { useState, useEffect } from 'react';
import axios from 'axios';

function NewNote() {
    const [message, setMessage] = useState("");
    const [messageCount, setMessageCount] = useState(0);

    const sendMessage = async () => {
        try {
        const response = await axios.post('http://localhost:5000/new', { message });
        setMessageCount(response.data.message_count);
        } catch (error) {
        console.log("error happened")
        console.error(error);
        }
    };

    const getMessageCount = async () => {
        try {
        //const response = await axios.get('http://localhost:5000/message_count');
        //setMessageCount(response.data.message_count);
        } catch (error) {
        console.error(error);
        }
    };

    useEffect(() => {
        getMessageCount();
    }, []);

    return (
        <div>
        <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} />
        <button onClick={sendMessage}>Send Ping</button>
        <p>Message Count: {messageCount}</p>
        </div>
    );
}

export default NewNote;
