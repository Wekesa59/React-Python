import React from "react";
import './App.css';
import SuperHeroList from './components/SuperHeros';

const App = () => {
    return (
        <div className="App">
          <header className="App-header">
            <h1> SuperHero Management App</h1>
          </header>
          <main>
            <SuperHeroList />
          </main>
        </div>
    );
};

export default App;
