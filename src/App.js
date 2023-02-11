import { React, useState, useEffect } from 'react'
import LiveData from './live_data.js';
import PastGames from './past_games.js';
import FutureMatchups from './future_matchups.js';
import './App.css';

function App() {
  const [game_type, setGameType] = useState();

  useEffect(() => {
    if (localStorage.gameType) {
      setGameType(localStorage.getItem("gameType"));
    } else {
      setGameType('live');
    }

    console.log('initial game type: ', game_type);
  }, []);

  function handleChange(e) {
    setGameType(e.target.value);
    localStorage.setItem('gameType', e.target.value);
  }

  return (
    <div className="App">
      <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@1,800&family=Quicksand&display=swap" rel="stylesheet"></link>
      {/* <header className="App-header"> </header> */}
      <div className="games">
        <div className="dropdown">
          <label for="gameType">Choose Game Day:</label>
          <select className="gameType" id="gameType" value={game_type} onChange={handleChange}>
            <option value="live">Today</option>
            <option value="past">Yesterday</option>
            <option value="future">Tomorrow</option>
          </select>
        </div>
        {game_type==='live' && <LiveData />}
        {game_type==='past' && <PastGames />}
        {game_type==='future' && <FutureMatchups />}
      </div>
    </div>
  );
}

export default App;