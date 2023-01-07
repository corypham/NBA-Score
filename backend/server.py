# Import flask and datetime module for showing date and time
from flask import Flask
import json
  
# Initializing flask app
app = Flask(__name__)

# flask
from nba_api.live.nba.endpoints import scoreboard

# # Today's Score Board
# games = scoreboard.ScoreBoard()

# # json
# games_json = games.get_json()

from datetime import datetime, timezone
from dateutil import parser
from dateutil.tz import gettz

f = "{gameId}: {awayTeam} vs. {homeTeam}" 
board = scoreboard.ScoreBoard()
print("ScoreBoardDate: " + board.score_board_date)
games = board.games.get_dict()
games_json = board.games.get_json()
game_data = [{}] * len(games)
# game_data = {}
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

# tzinfos = {"BRST": -7200, "CST": gettz("America/Cupertino")}
# for game in games:
#     gameTimeLTZ = parser.parse(game["gameTimeUTC"], tzinfo=timezone.utc).replace(tzinfo=timezone.utc).astimezone(tz=None)
#     print(f.format(gameId=game['gameId'], awayTeam=game['awayTeam']['teamName'], homeTeam=game['homeTeam']['teamName'], gameTimeLTZ=gameTimeLTZ))

# games_json = games.get_json()

from nba_api.stats.static import teams

nba_teams = teams.get_teams()

# Route for seeing a data
@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        # "teams": nba_teams,
        "games": json.dumps(game_data),
        # "details": games_json 
    }
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)