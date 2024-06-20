import React, { useState } from 'react';

function Home() {
    const [active, changeActive] = useState("NewNote");

    const renderContent = () => {
        if (active === "Home") {
            return <div>Welcome to the Home page!</div>;
        } else if (active === "NewNote") {
            return <div>Create a new note here.</div>;
        }
    };

    return (
        <div className="container">
            <header>
                <h1>Digital Diary</h1>
                <nav>
                    <a
                        href="#"
                        className={active === "Home" ? "active" : ""}
                        onClick={() => changeActive("Home")}
                    >
                        Home
                    </a>
                    <br />
                    <a
                        href="#"
                        className={active === "NewNote" ? "active" : ""}
                        onClick={() => changeActive("NewNote")}
                    >
                        New Note
                    </a>
                </nav>
            </header>
            <main>
                {renderContent()}
            </main>
        </div>
        )
}

export default Home;