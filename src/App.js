import { React, useState, useEffect } from 'react'
import axios from "axios";
import './App.css';

function App() {

   // new line start
  const [gameData, setGameScores] = useState(null);

  useEffect(() => {
    axios({
      method: "GET",
      url:"http://localhost:3000/data",
    })
    .then((response) => {
      const res = response.data
      setGameScores(({
        games: JSON.parse(res.games),
      }))
      console.log(res.games);
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
      }
    })
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {gameData && (gameData.games).map((game) => (
          <div className="game">
              <div className="vs">{game.awayTeamData.name} v {game.homeTeamData.name}</div>
              <div className="teamA">
                <div className="name">{game.awayTeamData.name}</div>
                <div className="score">{game.awayTeamData.score}</div>
              </div>
              <div className="teamB">
                <div className="name">{game.homeTeamData.name}</div>
                <div className="score">{game.homeTeamData.score}</div>
              </div>
              <div className="gametatus">{game.gameStatus}</div>
              </div>
        ))}
      </header>
    </div>
  );
}

export default App;