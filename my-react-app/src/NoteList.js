import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './NoteList.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';

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
      <div className="note-container">
        {notes.map((note) => (
          <div className="note" key={note.id}>
            <div className="note-header">
              <span className="note-date">{note.date}</span>
              <FontAwesomeIcon icon={faTrashAlt} className="delete-icon" onClick={() => deleteNote(note.id)} />
            </div>
            <div className="note-content">{note.message}</div>
          </div>
        ))}
      </div>
    );
};

export default NoteList;