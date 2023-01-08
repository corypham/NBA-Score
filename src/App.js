import { React, useState, useEffect } from 'react'
import axios from "axios";
import './App.css';

function App() {

   // new line start
  const [gameData, setGameScores] = useState(null);

  let today = new Date().toLocaleDateString();
  let new_date = new Date(today);

  function get_live_data() {
    axios({
      method: "GET",
      url:"/data",
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
  }

  useEffect(() => {
    get_live_data();
  }, []);

  return (
    <div className="App">
      <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@1,800&family=Quicksand&display=swap" rel="stylesheet"></link>
      <header className="App-header">
        <div className="games">
          <div className="date">{today}</div>
          {gameData && (gameData.games).map((game) => (
            <div className="game">
                <div className="vs teamName">{game.awayTeamData.name} v {game.homeTeamData.name}</div>
                <div className="teams">
                  <div className="teamA team">
                    <img className="logo" src={require(`./assets/${game.awayTeamData.logoURL}.png`)} alt=""/>
                    <div className="name teamName">{game.awayTeamData.name}</div>
                    <div className="score">{game.awayTeamData.score}</div>
                  </div>
                  <div className="vl"></div>
                  <div className="teamB team">
                    <img className="logo" src={require(`./assets/${game.homeTeamData.logoURL}.png`)} alt=""/>
                    <div className="name teamName">{game.homeTeamData.name}</div>
                    <div className="score">{game.homeTeamData.score}</div>
                  </div>
                </div>
                <div className="gametatus">{game.gameStatus}</div>
            </div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;