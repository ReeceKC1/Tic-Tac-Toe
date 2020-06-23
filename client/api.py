import requests

#  requests.port/get('address', data = {})

SERVER_ADDRESS = 'http://localhost:5000'



def login_api(username, password):
    # hash password

    response = requests.post(f"{SERVER_ADDRESS}/c4/login", json={
        'name': username,
        'password': password
    })

    if response.status_code == 400:
        return response.json().get('error')
    return ''

def signup_api(username, password):
    # hash password

    response = requests.post(f"{SERVER_ADDRESS}/c4/signup", json={
        'name': username,
        'password': password
    })

    if response.status_code == 400:
        return response.json().get('error')
    return ''

def get_leaderboard_api():
    response = requests.get(f"{SERVER_ADDRESS}/c4/leaderboard", json={
        'offset': 0
    })
    if response.status_code == 400:
        print(response.json().get('error'))
    return response.json().get('leaderboard')

def post_record_api(winner, loser):
    response = requests.post(f"{SERVER_ADDRESS}/c4/leaderboard", json={
        'winner': winner.name,
        'loser': loser.name
    })