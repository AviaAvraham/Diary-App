import React, { useState } from 'react';
import NewNote from './NewNote.js';
import NoteList from './NoteList';
import './Home.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPenToSquare } from '@fortawesome/free-solid-svg-icons';

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
            <img src="https://d1nhio0ox7pgb.cloudfront.net/_img/g_collection_png/standard/32x32/leaf.png"
            style={{ width: '32px', height: '32px', marginRight: '10px', marginTop: '30px' }}/>
            <h1>TheraPrompt</h1>
            <a
                href="#"
                className={active === "NewNote" ? "active" : ""}
                onClick={() => active === "NewNote" ? setActive("Home") : setActive("NewNote")}
                style={{ color: active === "NewNote" ? '#007bff' : '#000000', textDecoration: 'none', display: 'flex', alignItems: 'center', marginLeft: '10px'}}
            >
                <FontAwesomeIcon icon={faPenToSquare} />
            </a>
        </nav>
    );
};

export default Home;
