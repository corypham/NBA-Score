import { React, useState, useEffect } from 'react'
import Scores from './scores.js';
import axios from "axios";
import './live_data.css'; // change this later

function PastGames() {

   // new line start
  const [gameData, setGameScores] = useState(null);

  let yesterday = new Date().toLocaleDateString() - 1;

  function get_past_games() {
    axios({
      method: "GET",
      url:"/data/past",
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
    get_past_games();
  }, []);

  return (
        <div className="pastGames">
          <div className="date">{yesterday}</div>
          {gameData && (gameData.games).map((games_now) => (
            (games_now.game_data).map((game) => (
              <Scores game={game} />
            ))
          ))}
        </div>
  );
}

export default PastGames;