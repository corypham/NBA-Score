import { React, useState, useEffect } from 'react'
import Scores from './scores.js';
import axios from "axios";
import './App.css';

function LiveData() {

   // new line start
  const [gameData, setGameScores] = useState(null);

  let today = new Date().toLocaleDateString();

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
            <Scores game={game} />
          ))}
        </div>
      </header>
    </div>
  );
}

export default LiveData;