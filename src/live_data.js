import { React, useState, useEffect } from 'react'
import Scores from './scores.js';
import axios from "axios";
import './live_data.css';

function LiveData() {

   // new line start
  const [gameData, setGameScores] = useState(null);

  let today = new Date().toLocaleDateString();

  function get_live_data() {
    axios({
      method: "GET",
      url: "http://localhost:5000/data/live",
      headers: { 'Access-Control-Allow-Origin': "http://localhost:5000" }
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
        <div className="liveData">
          <div className="date">{today}</div>
          {gameData && (gameData.games).map((game) => (
            <Scores game={game} />
          ))}
        </div>
  );
}

export default LiveData;