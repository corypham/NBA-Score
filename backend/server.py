# Import flask and datetime module for showing date and time
from flask import Flask
import json
  
# Initializing flask app
app = Flask(__name__)

# flask

from datetime import datetime, timezone, date, timedelta
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

# Route for seeing live data
@app.route('/data/live')
def get_live_data():
    game_data = fetch()
    return {
        "games": json.dumps(game_data),
    }

# get past games
from nba_api.stats.endpoints import scoreboard as pastscores
def get_past_games():
    today = date.today()
    board = pastscores.Scoreboard(day_offset='-1')
    past_games_json = board.get_json()
    #  = board.get_dict()
    # game_data = [{}] * len(games)
    # test = [{}] * len(games.games.resource.resultSets.name.rowSet)
    # # past_week_data = [{}] * 2
    # for i in range (len(games.games.resource.resultSets.name.rowSet)):
    #     test[i] = games.games.resource.resultSets.name.rowSet[i]
    # for i in range (2):
    #     week_games = games[games.LAST_GAME_DATE_EST=='2023-01-08']
    #     past_week_data[i] = {
    #         "date": today,
    #         "games": week_games,
    #     }

    #             "gameStatus": (games[i])['gameStatusText'],
    #             "awayTeamData": {
    #                 "logoURL": './assets/' + (games[i])['awayTeam']['teamTricode'] + '.png',
    #                 "logoURL": (games[i])['awayTeam']['teamTricode'],
    #                 "name": (games[i])['awayTeam']['teamName'],
    #                 "score": (games[i])['awayTeam']['score']
    #                 }, 
    #             "homeTeamData": {
    #                 "logoURL": (games[i])['homeTeam']['teamTricode'],
    #                 "name": (games[i])['homeTeam']['teamName'],
    #                 "score": (games[i])['homeTeam']['score']
    #                 }, 
    #             }
    #         }
    #     print("hello world", game_data[i]['awayTeamData']['logoURL'])
    return past_games_json

# Route for seeing past games
@app.route('/data/past')
def get_past_data():
    past_games = get_past_games()
    return {
        "games": json.dumps(past_games),
    }

# get future matchups
def get_future_matchups():
    print("WIP")
  
# Running app
if __name__ == '__main__':
    app.run(debug=True)