from flask import *
from server.database import *
import re
import traceback
from sqlalchemy.sql import func

app = Flask(__name__)

RECORD_LIMIT = 50
NAME_REGEX = "[0-9a-zA-Z]+"

# login
# signup
# play_global
# get leaderboard
# add leaderboard

# get player
#   create session: session = Session()
#   query database using session.query().filter_by().all()

# add player
#   create session: session = Session()
#   create player object
#   add player to session
#   commit session


@app.route("/c4/login", methods=['POST'])
def login():
    data = request.json
    name = data['name']
    password = data['password']
    user = Player(name=name, password=password)
    session = Session()

    try:
        # Checking for user in database
        result = session.query(Player).filter_by(name=name).one_or_none()
        if result:
            # Checking if passwords match
            if password == result.password:
                return jsonify({'success': "Successfully logged in"}), 200
            else:
                raise Exception("login failed, password was incorrect")
        else:
            raise Exception("login failed, user not found")
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        session.close()
        
    

@app.route("/c4/signup", methods=['POST'])
def signup():
    session = Session()
    try:
        name = request.json.get('name')
        password = request.json.get('password')

        # Validate name and password
        if not re.match(NAME_REGEX, name):
            raise Exception("Name regex does not match")
        if session.query(Player).filter_by(name=name).all():
            raise Exception("Player already exists")

        player = Player(name = name, password = password)
        session.add(player)
        session.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        session.close()

@app.route("/c4/playglobal", methods=['GET'])
def play_global():
    pass

@app.route("/c4/leaderboard", methods=['GET', 'POST'])
def leaderboard():
    session = Session()
    try:
        if request.method == 'GET': 
            offset = request.json.get('offset')
            # Querying for list of players with their amount of wins sorted in descending order
            leaders = session.execute(text(f"SELECT winner, COUNT(winner) \
                                            FROM record \
                                            GROUP BY winner \
                                            ORDER BY 2 DESC \
                                            LIMIT {RECORD_LIMIT} OFFSET {offset}")).fetchall()
            leaders = [Record(**x).serialize for x in leaders]
            return jsonify({'leaderboard': leaders})
        elif request.method == 'POST':
            winner = request.json.get('winner')
            loser = request.json.get('loser')
            # Checking if winner exists
            if not winner or not session.query(Player).filter_by(name=winner).all():
                raise Exception(f"Winner {winner} does not exist")
            # Checking if loser exists
            if not loser or not session.query(Player).filter_by(name=loser).all():
                raise Exception(f"Loser {loser} does not exist")
            # Adding record to database
            record = Record(winner = winner, loser = loser, date_time=func.now())
            session.add(record)
            session.commit()
            return jsonify({'success': 'successfully added record'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug = True)