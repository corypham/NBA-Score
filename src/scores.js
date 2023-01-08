import { React, useState, useEffect } from 'react'
import axios from "axios";
import './scores.css';

function Scores(props) {
  return (
            <div className="game">
                <div className="vs teamName">{props.game.awayTeamData.name} v {props.game.homeTeamData.name}</div>
                <div className="teams">
                  <div className="teamA team">
                    <img className="logo" src={require(`./assets/${props.game.awayTeamData.logoURL}.png`)} alt=""/>
                    <div className="name teamName">{props.game.awayTeamData.name}</div>
                    <div className="score">{props.game.awayTeamData.score}</div>
                  </div>
                  <div className="vl"></div>
                  <div className="teamB team">
                    <img className="logo" src={require(`./assets/${props.game.homeTeamData.logoURL}.png`)} alt=""/>
                    <div className="name teamName">{props.game.homeTeamData.name}</div>
                    <div className="score">{props.game.homeTeamData.score}</div>
                  </div>
                </div>
                <div className="gameStatus">{props.game.gameStatus}</div>
            </div>
  );
}

export default Scores;