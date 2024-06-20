// PromptGenerator.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSync } from '@fortawesome/free-solid-svg-icons';

const PromptGenerator = () => {
    const [prompt, setPrompt] = useState("Generating prompt...");

    // Function to fetch a new prompt from the server
    const fetchPrompt = async () => {
        try {
            const response = await axios.get('http://localhost:5000/prompt');
            console.log(response.data)
            setPrompt(response.data.prompt.answer);
        } catch (error) {
            console.error("Error fetching prompt:", error);
        }
    };

    // Fetch initial prompt on component mount
    useEffect(() => {
        fetchPrompt();
    }, []);

    return (
        <div className="prompt-container">
            <div className="prompt-content">
                <span>{prompt}</span>
                <button onClick={fetchPrompt} style={{marginLeft:"10px"}}>
                    <FontAwesomeIcon icon={faSync} />
                </button>
            </div>
        </div>
    );
};

export default PromptGenerator;
