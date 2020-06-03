from client.token import Token

# Board for playing connect 4
class Board:
    DEFAULT_ROW = 7
    DEFAULT_COLUMN = 6
    # row
    # column
    # Active Tokens

    # Constructor taking a row and column
    # @row the number of rows, default DEFAULT_ROW
    # @row the number of columns, default DEFAULT_COLUMN
    def __init__(self, row = DEFAULT_ROW, column = DEFAULT_COLUMN):
        self.row = row
        self.column = column
        self.active_tokens = []

    # Adds a token to the game board
    # @player the player taking the turn
    # @column the column to add the token to
    def add_token(self, player, column):
        # Vaidating column
        if column < 0 or column >= self.column:
            raise Exception(f"Invalid column {column}.")
        # Getting token row and checking if row is full
        new_row = self.gravity(column)
        if new_row == self.row:
            raise Exception("Column is full.")
        # Adding token
        self.active_tokens.append(Token(new_row, column, player))
    
    # Checks rows within the column and looks for lowest row.
    # @return the destination row.
    def gravity(self, column):
        # Getting items in column
        temporary = [x for x in self.active_tokens if x.column == column]
        # Sorting items by row
        temporary.sort(key = lambda x: x.row)
        # Want gravity to return row.        
        return temporary[-1].row + 1 if temporary else 0        

    # Clears the current board
    def clear(self):
        self.active_tokens = []

    def check_win(self):
        # To check win, need to check win conditions in every
        # direction. These will be called in here.
        # 
        pass

    def win_left(self):
        # Need to look at last piece placed.
        # For this specific condition, we want to see
        # if the tokens on the left of the played piece exist.
        # To check this, look at the token played.
        # With the same row, player attribute,
        # Look for column -1, -2, -3 and see if they exist in
        # active tokens.
        # @return True or False based on if exists.

        # Attempt at recursive function:
        # Base function where we'd want to stop executing would be a four match.
        # Initialize function with count 0.
        # Check should return an increased count and call the function.
        # Calling of that win condition should continue until
        # base condition is met or piece isn't in active token.
        # Function resetscount each time new win condition called.        
        # Function will then call next condition, continuing
        # until all conditions have been checked. 
        # Once checked, control returns to opposite player.
        pass

    # Dunder String method that handles printing the board
    def __str__(self):
        # print out board with tokens
        board = ""
        # Printing board from highest to lowest row
        for i in reversed(range(0,self.row)):
            board += "|"
            for j in range(0, self.column - 1):
                board += "=|"
            board += "=|\n|"
            # Getting only tokens in the current row
            column_data = [x for x in self.active_tokens if x.row == i]
            for j in range(0,self.column):
                # Gets token with matching column and either adds the token or empty
                token = [x for x in column_data if x.column == j]
                if token:
                    board += f"{token[0]}|"
                else:
                    board += "_|"
            board += "\n"
        # Adding numbers on bottom
        for i in range(0, self.column):
            board += " " + str(i)
        return board