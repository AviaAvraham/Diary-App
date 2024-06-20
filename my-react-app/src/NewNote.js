import React, { useState } from 'react';

function NewNote() {
    const [note, setNote] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        alert(`Note submitted: ${note}`);
        // Here you can add logic to handle the note submission, like sending it to a server
        setNote(""); // Clear the textarea after submission
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="note">New Note:</label>
                <textarea
                    id="note"
                    value={note}
                    onChange={(e) => setNote(e.target.value)}
                    rows="4"
                    cols="50"
                />
            </div>
            <button type="submit">Submit</button>
        </form>
    );
}

export default NewNote;
