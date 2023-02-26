# Imports
from flask import Flask
import json
import math
from datetime import datetime, timezone, date, timedelta
from flask_cors import CORS

from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.static import teams
from nba_api.stats.endpoints import scoreboard as board_of_scores
# Initializing flask app
app = Flask(__name__)

cors = CORS(app)

def get_date(num_days):
    if num_days == -1:
        return 'Yesterday'
    elif num_days == 1:
        return 'Tomorrow'
    elif num_days == 0:
        return 'Today'
    else:
        today = date.today()
        day = today + timedelta(days = num_days)
        return day.strftime('%m/%d/%Y')

# fetch live data
def fetch():
    board = scoreboard.ScoreBoard()
    print("ScoreBoardDate: " + board.score_board_date)
    today = date.today()
    if board.score_board_date == today:
        games = board.games.get_dict()
        game_data = [{}] * len(games)
        for i in range (len(games)):
            game_data[i] = {
                "gameStatus": (games[i])['gameStatusText'],
                "awayTeamData": {
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
    else:
        board = board_of_scores.Scoreboard()
        live_games = board.get_normalized_dict()
        pg = live_games['LineScore']
        s = live_games['GameHeader']

        game_data = [{}] * (math.ceil(len(pg)/2))
        for i in range (math.ceil(len(pg)/2)):
            game_data[i] = {
                "gameDate": (s[i])['GAME_DATE_EST'],
                "gameStatus": (s[i])['GAME_STATUS_TEXT'],
                "awayTeamData": {
                    "logoURL": (pg[2*i])['TEAM_ABBREVIATION'],
                    "name": teams.find_team_name_by_id((pg[2*i])['TEAM_ID'])['nickname'],
                    "score": (pg[2*i])['PTS'],
                    }, 
                "homeTeamData": {
                    "logoURL": (pg[2*i+1])['TEAM_ABBREVIATION'],
                    "name": teams.find_team_name_by_id((pg[2*i+1])['TEAM_ID'])['nickname'],
                    "score": (pg[2*i+1])['PTS'],
                    }, 
                }
    return game_data

# Route for seeing live data
@app.route('/data/live')
def get_live_data():
    game_data = fetch()
    return {
        "games": json.dumps(game_data),
    }

# get past games
def get_past_games():
    today = date.today()
    past_game_data = [{}] * 1

    for d in range (0, 1):
        num_offset = (d * (-1)) - 1
        board = board_of_scores.Scoreboard(day_offset=num_offset)
        past_games = board.get_normalized_dict()
        pg = past_games['LineScore']

        game_data = [{}] * (math.ceil(len(pg)/2))
        for i in range (math.ceil(len(pg)/2)):
            game_data[i] = {
                # "gameStatus": (pg[i])['GAME_STATUS_TEXT'],
                "gameDate": (pg[2*i])['GAME_DATE_EST'],
                "gameStatus": 'Final',
                "awayTeamData": {
                    "logoURL": (pg[2*i])['TEAM_ABBREVIATION'],
                    "name": teams.find_team_name_by_id((pg[2*i])['TEAM_ID'])['nickname'],
                    "score": (pg[2*i])['PTS']
                    }, 
                "homeTeamData": {
                    "logoURL": (pg[2*i+1])['TEAM_ABBREVIATION'],
                    "name": teams.find_team_name_by_id((pg[2*i+1])['TEAM_ID'])['nickname'],
                    "score": (pg[2*i+1])['PTS']
                    }, 
                }
        past_game_data[d] = {
            'game_day': get_date(num_offset),
            'offset': num_offset,
            'game_data': game_data,
        }
    return past_game_data


# Route for seeing past games
@app.route('/data/past')
def get_past_data():
    past_games = get_past_games()
    return {
        "games": json.dumps(past_games),
    }

# get future matchups
def get_future_matchups():
    today = date.today()
    future_game_data = [{}] * 1

    for d in range (0, 1):
        num_offset = d + 2 #change this back to 1
        board = board_of_scores.Scoreboard(day_offset=num_offset)
        future_games = board.get_normalized_dict()
        pg = future_games['LineScore']
        s = future_games['GameHeader']

        game_data = [{}] * (math.ceil(len(pg)/2))
        for i in range (math.ceil(len(pg)/2)):
            game_data[i] = {
                "gameDate": (s[i])['GAME_DATE_EST'],
                "gameStatus": (s[i])['GAME_STATUS_TEXT'],
                "awayTeamData": {
                    "logoURL": (pg[2*i])['TEAM_ABBREVIATION'],
                    "name": teams.find_team_name_by_id((pg[2*i])['TEAM_ID'])['nickname'],
                    "score": '-'
                    }, 
                "homeTeamData": {
                    "logoURL": (pg[2*i+1])['TEAM_ABBREVIATION'],
                    "name": teams.find_team_name_by_id((pg[2*i+1])['TEAM_ID'])['nickname'],
                    "score": '-'
                    }, 
                }
        future_game_data[d] = {
            'game_day': get_date(num_offset),
            'offset': num_offset,
            'game_data': game_data,
        }
    return future_game_data

# Route for seeing future games
@app.route('/data/future')
def get_future_data():
    future_games = get_future_matchups()
    return {
        "games": json.dumps(future_games),
    }
  
# Running app
if __name__ == '__main__':
    app.run(debug=True)