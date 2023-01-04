# Import flask and datetime module for showing date and time
from flask import Flask
import datetime
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)

# flask
from nba_api.live.nba.endpoints import scoreboard

# Today's Score Board
games = scoreboard.ScoreBoard()

# json
games_json = games.get_json()
  
# Route for seeing a data
@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        "games":games_json
    }
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)