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
            <div style={{display:"flex"}} className="container mx-auto p-4 bg-white bg-opacity-80 rounded-lg shadow-lg">
            {/* <header className="text-center py-4"> */}
                <img src="/public/images/logo.png"
                    style={{ width: '32px', height: '32px', marginRight: '10px', marginTop: '5px' }}/>
                    
                        
                            <h1>TheraPrompt</h1>
                            
                            <a
                                href="#"
                                className={active === "NewNote" ? "active" : ""}
                                onClick={() => active === "NewNote" ? setActive("Home") : setActive("NewNote")}
                                style={{ color: active === "NewNote" ? '#007bff' : '#000000', textDecoration: 'none', display: 'flex', alignItems: 'center', marginLeft: '10px'}}
                            >
                                <FontAwesomeIcon icon={faPenToSquare} />
                            </a>
                            {/* </header> */}
            </div>
        </nav>
    );
};

export default Home;
