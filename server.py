from Flask import *
from database import *

app = Flask(__name__)

# login
# signup
# play_global
# get leaderboard
# add leaderboard

@app.route("/c4/login/", methods=['POST'])
def login():
    data = request.json
    name = data['name']
    password = data['password']
    pass

@app.route("/c4/signup/", methods=['POST'])
def signup():
    session = Session()
    try:
        name = request.args.get('name')
        password = request.args.get('password')

        if '5' in name:
            raise Exception("Fuck the number 5")

        player = Player(name = name, password = password)
        session.add(player)
        session.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        session.close()

@app.route("/c4/playglobal/", methods=['GET'])
def play_global():
    pass

@app.route("/c4/leaderboard/", methods=['GET', 'POST'])
def leaderboard():
    pass