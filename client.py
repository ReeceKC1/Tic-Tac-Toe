from client.board import Board
from client.game import Game
from client.player import Player
import sys
import os

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
            '3': lambda : show_leaderboards(),
            '4': lambda : exit()
        }.get(value)()
    # If the user is logged in
    else:
        return {
            '1': lambda : login(), #Maybe add a logout option?
            '2': lambda : play_local(),
            '3': lambda : play_global(),
            '4': lambda : exit()
        }.get(value)

def login():
    # Takes input from user.
    # Check playerbase to see if name in playerbase. Break if not found
    # If found, return, "Player Found"
    # Ask for password. If successful, print "Logged into player name"
    # If not found loop again. Max number of tries.
    # @return to main menu.
    print("In the login function")

def signup():
    # Takes an input from user. 
    # If input is in playerbase, print "Name has already been taken."
    # If input is not in playerbase, ask user to input password with.an
    # Ask player to confirm password.
    # If valid, print, "Player name has been added to leaderbase."
    # @return to main menu.
    print("in signup")

def play_local():
    # Launches an instance of the game.
    ai = Player
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
    os.system('cls')
    os.system('clear')
    # Printing out menu for players
    if not user:
        input_value = input("""
Hello guest, welcome to Connect 4!
Please select an option below:
1. Login
2. Signup
3. Show Leaderboards
4. Exit
""" + error_message)
    else:
        input_value = input(f"""
Hello, {user.name}, welcome to Connect 4!
Please select an option below:
1. Play local
2. Play Global
3. Show Leaderboards
4. Exit
""" + error_message) 
    # Interpreting input and handling errors
    try:
        switch(input_value)
        error_message = ""
    except Exception as e:
        error_message = "***Invalid option, please try again***"