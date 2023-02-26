import { React, useState, useEffect } from 'react'
import Scores from './scores.js';
import axios from "axios";
import './live_data.css'; //change this later

function FutureMatchups() {

   // new line start
  const [gameData, setGameScores] = useState(null);

  let tomorrow = new Date(new Date().setDate(new Date().getDate()+1)).toLocaleDateString();

  function get_future_matchups() {
    axios({
      method: "GET",
      url:"http://localhost:5000/data/future",
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
    get_future_matchups();
  }, []);

  return (
        <div className="futureMatchups">
          <div className="date">{tomorrow}</div>
          {gameData && (gameData.games).map((games_now) => (
            (games_now.game_data).map((game) => (
              <Scores game={game} />
            ))
          ))}
        </div>
  );
}

export default FutureMatchups;