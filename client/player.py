# Parent class for all Player types
class Player:
    # Used to prompt the Player for input with a message
    def prompt(self, text):
        pass
    # Used to send a message to the Player
    def display(self, text):
        pass

# Local Player using the command line
class LocalPlayer(Player):
    # Constructor
    def __init__(self, name = "Guest"):
        self.name = name
    # Prompts a console input
    def prompt(self, text):
        return input(text)
    # Displays a message for the player
    def display(self, text):
        print(text)

    def __str__(self):
        return self.name

# Remote Player to be handled by the server
class RemotePlayer(Player):
    def prompt(self, text):
        pass
    def display(self, text):
        pass

# AI Player designed to compete against players
class AiPlayer(Player):
    def prompt(self, text):
        pass
    def display(self, text):
        pass
