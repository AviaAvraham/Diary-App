import React, { useState, useEffect } from 'react';
import axios from 'axios';

const NoteList = ({ editNote, deleteNote }) => {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/getNotes');
        setNotes(response.data); // Update notes state with fetched data
      } catch (error) {
        console.error(error);
      }
    };

    fetchData(); // Call fetchData function when component mounts
  }, []); // Empty dependency array ensures this effect runs only once on mount

  console.log("notes are ", notes);

  return (
    <div>
      {notes.map((note) => (
        <div key={note.id}>
          <p>{note.date + ": " + note.message}</p>
          <button onClick={() => deleteNote(note.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
};

export default NoteList;