import React from 'react';

const NoteList = ({ notes, editNote, deleteNote }) => {
  return (
    <div>
      {notes.map((note) => (
        <div key={note.id}>
          <p>{note.content}</p>
          <button onClick={() => editNote(note)}>Edit</button>
          <button onClick={() => deleteNote(note.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
};

export default NoteList;
