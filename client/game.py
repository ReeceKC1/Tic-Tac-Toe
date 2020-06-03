from client.board import Board
import random 


class Game:
    # Needs to handle the players turn
    # Needs to handle who goes first
    # These are the columns you can choose, or this to exit. 
    # Limit full columns.

    # Constructor taking 2 players
    # @player1 the first player
    # @player2 the second player
    def __init__(self, player1, player2):
        # Need to create two players and a gameboard.
        self.player1 = player1
        self.player2 = player2
        self.gameboard = Board()

    # Game setup and coin toss
    def start(self):
        # Variable for looping until user enters heads or tails
        done = False
        # Flips the coin
        coin_toss = random.randint(0, 1)
        # Asking user for coin toss until correctly input
        while not done:
            heads_tails = self.player1.prompt(f"{self.player1.name}: Pick heads (h) or tails (t). ")
            # If the user enters correct data
            if heads_tails == "h" or heads_tails == "l":
                if not (coin_toss == 0 and heads_tails == "h" or coin_toss == 1 and heads_tails == "t"):
                    self.player1, self.player2 = self.player2, self.player1
                done = True
            else:
                self.player1.display("Invalid option, please try again")
        # Outputs player order to the run function.
        self.run()

    # Players taking turns dropping tokens
    def run(self):
        # Determines the turn and the current player dropping
        turn_count = 0
        # While no player has won
        while not self.gameboard.check_win():
            prompt_message = "Please select a column to drop"
            done = False
            # Set the current player to either player1 or player2 based on the counter
            if turn_count % 2 == 0:
                player = self.player1
            else:
                player = self.player2
            # Loops for input until the user gets a correct column
            while not done:
                player.display(self.gameboard)
                try:
                    column = player.prompt(f"{player}: Select a Column to drop a token ")
                    self.gameboard.add_token(player, int(column))
                    done = True
                except Exception as e:
                    player.display(f"Error: {e} Please select a new column")
            # Incrementing current play counter
            turn_count += 1