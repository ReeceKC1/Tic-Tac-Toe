from client.board import Board
from client.game import Game
from client.player import *
import sys
import os
from client.api import *
from getpass import getpass

user = None
error_message = ""

# A switch value for console input
# @value the input from console
def switch(value):
    # If the user is not logged in
    # Creates a dictionary and then selects a value based on the input
    if not user:
        return {
            '1': lambda : login(),
            '2': lambda : signup(),
            '3': lambda : play_local_pvp(),
            '4': lambda : show_leaderboards(),
            '5': lambda : exit()
        }.get(value)()
    # If the user is logged in
    else:
        return {
            '1': lambda : play_local_pvai(),
            '2': lambda : play_local_pvp(),
            '3': lambda : play_global(),
            '4': lambda : show_leaderboards(),
            '5': lambda : logout(),
            '6': lambda : exit()
        }.get(value)()

def login():
    global user
    username = ""
    print("Please enter your credentials to login")
    while (response := login_api(username := input("Username: "), getpass("Password: "))):
        print(f"Error: {response}")
    print("Successfully logged in")
    user = LocalPlayer(username)

def logout():
    global user
    user = None

def signup():
    global user
    print("in signup")
    print("Please enter a username and password to signup.")
    while (response := signup_api(username := input("Username: "), getpass("Password: "))):
        print(f"Error: {response}")
    print("Successfully signed up.")
    user = LocalPlayer(username)

def play_local_pvp():
    # Launches an instance of the game.
    if user:
        game = Game(user, LocalPlayer())
    else:
        game = Game(LocalPlayer(), LocalPlayer("Other"))
    game.start()

def play_local_pvai():
    ai = AiPlayer()
    game = Game(user, ai)
    game.start()

def play_global():
    # Connects to server, looks for another player to match to.
    pass

def show_leaderboards():
    # query server
    pass

def exit():
    # Either exit in single player, or send a message if multiplayer.
    sys.exit()

while True:
    # Clearing console
    # os.system('cls')
    # os.system('clear')
    # Printing out menu for players
    print(user)
    if not user:
        input_value = input("""
Hello guest, welcome to Connect 4!
Please select an option below:
1. Login
2. Signup
3. Play local PvP
4. Show Leaderboards
5. Exit
""" + error_message)
    else:
        input_value = input(f"""
Hello, {user}, welcome to Connect 4!
Please select an option below:
1. Play local PvAI
2. Play local PvP
3. Play Global
4. Show Leaderboards
5. Logout
6. Exit
""" + error_message) 
    # Interpreting input and handling errors
    try:
        switch(input_value)
        error_message = ""
    except Exception as e:
        error_message = f"{e}\n***Invalid option, please try again***"