import React, { useState } from 'react';
import NewNote from './NewNote.js';
import NoteList from './NoteList';
import './Home.css';

function Home() {
    const [active, setActive] = useState("Home");

    const renderContent = () => {
        if (active === "Home") {
            return <NoteList />;
        } else if (active === "NewNote") {
            return <NewNote />;
        }
    };

    return (
        <div className="container">
            <header>
                <h1>Digital Diary</h1>
                <Navigation active={active} setActive={setActive} />
            </header>
            <main>
                {renderContent()}
            </main>
        </div>
    );
}

const Navigation = ({ active, setActive }) => {
    return (
        <nav>
            <a
                href="#"
                className={active === "Home" ? "active" : ""}
                onClick={() => setActive("Home")}
            >
                Home
            </a>
            <span> - - </span>
            <a
                href="#"
                className={active === "NewNote" ? "active" : ""}
                onClick={() => setActive("NewNote")}
            >
                New Note
            </a>
        </nav>
    );
};

export default Home;
