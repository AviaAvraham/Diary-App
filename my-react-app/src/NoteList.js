import React, { useState } from 'react';
import axios from 'axios';

const NoteList = ({editNote, deleteNote }) => {
  const [notes, setNotes] = useState([]);
  const getNotes = async () => {
    try {
      const response = await axios.get('http://localhost:5000/getNotes');
      return response.data;
    } catch (error) {
      console.error(error);
    }
  };
  
  getNotes().then((data) => {
    notes = data;
    console.log("notes aren't " + notes); // Log the notes after they are fetched
  });
  console.log("notes are " + notes)
  return (
    <div>
      {notes.map((notes) => (<div></div>))}
      {/* {notes.map((note) => (
        <div key={note.id}>
          <p>{note.content}</p>
          <button onClick={() => editNote(note)}>Edit</button>
          <button onClick={() => deleteNote(note.id)}>Delete</button>
        </div>
      ))} */}
    </div>
  );
};

export default NoteList;
