# Import flask and datetime module for showing date and time
from flask import Flask
import json
  
# Initializing flask app
app = Flask(__name__)

# flask

from datetime import datetime, timezone
from dateutil import parser
from dateutil.tz import gettz

# fetch live data
from nba_api.live.nba.endpoints import scoreboard
def fetch():
    board = scoreboard.ScoreBoard()
    print("ScoreBoardDate: " + board.score_board_date)
    games = board.games.get_dict()
    # games_json = board.games.get_json()
    game_data = [{}] * len(games)
    for i in range (len(games)):
        game_data[i] = {
            "gameStatus": (games[i])['gameStatusText'],
            "awayTeamData": {
                # "logoURL": './assets/' + (games[i])['awayTeam']['teamTricode'] + '.png',
                "logoURL": (games[i])['awayTeam']['teamTricode'],
                "name": (games[i])['awayTeam']['teamName'],
                "score": (games[i])['awayTeam']['score']
                }, 
            "homeTeamData": {
                "logoURL": (games[i])['homeTeam']['teamTricode'],
                "name": (games[i])['homeTeam']['teamName'],
                "score": (games[i])['homeTeam']['score']
                }, 
            }
        print("hello world", game_data[i]['awayTeamData']['logoURL'])
    return game_data

# get past games
from nba_api.stats.endpoints import leaguegamefinder
def get_past_games():
    print("WIP")

# get future matchups
def get_future_matchups():
    print("WIP")

# Route for seeing a data
@app.route('/data')
def get_time():
    game_data = fetch()
    return {
        "games": json.dumps(game_data),
        # "details": games_json 
    }
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)