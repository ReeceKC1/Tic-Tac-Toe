from client.board import Board
import random 


class Game:
    # Needs to handle the players turn
    # Needs to handle who goes first
    # These are the columns you can choose, or this to exit. 
    # Limit full columns.

    def __init__(self, player1, player2):
        # Need to create two players and a gameboard.
        self.player1 = player1
        self.player2 = player2
        self.gameboard = Board()

    # Game setup and coin toss
    def start(self):
        # Use random module to flip a coin.
        # Player 1 calls heads or tails.
        # First pick is odds, second pick is evens.
        # Display turn in bottom area, decide who's turn it is through %
        heads_tails = self.player1.prompt(f"{self.player1.name}: Pick heads (h) or tails (t).")
        coin_toss = random.randint(0, 1)
        # Initialize turn_count to 0. After coin toss, add 1 to turn_count after every turn.
        # If win coin toss, turn_count % 2 == 1 for player1, turn_count % 2 == 0 for player2.

        if not (coin_toss == 0 and heads_tails == "h" or coin_toss == 1 and heads_tails == "t"):
            self.player1, self.player2 = self.player2, self.player1

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
                try:
                    column = player.prompt("Select a Column to drop a token ")
                    self.gameboard.add_token(player1, column)
                    done = True
                except Exception as e:
                    prompt_message = f"Error: {e} Please select a new column".format(e)
                print(self.gameboard)
            # Incrementing current play counter
            turn_count += 1