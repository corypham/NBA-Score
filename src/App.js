import { useState } from 'react'
import axios from "axios";
import './App.css';

function App() {

   // new line start
  const [games, setGameScores] = useState(null)

  function getData() {
    axios({
      method: "GET",
      url:"http://localhost:3000/data",
    })
    .then((response) => {
      const res = response.data
      setGameScores(({
        games: res.games,
      }))
      console.log(res);
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
    //end of new line 

  return (
    <div className="App">
      <header className="App-header">
        <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {games && <div>
              <p>games: {games.games}</p>
            </div>
        }
      </header>
    </div>
  );
}

export default App;