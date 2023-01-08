import { React, useState, useEffect } from 'react'
import LiveData from './live_data.js';
import axios from "axios";
import './App.css';

function App() {

  return (
    <div className="App">
      <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@1,800&family=Quicksand&display=swap" rel="stylesheet"></link>
      <header className="App-header">
        <LiveData />
      </header>
    </div>
  );
}

export default App;