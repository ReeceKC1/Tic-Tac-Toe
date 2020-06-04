from client.token import Token

# Board for playing connect 4
class Board:
    DEFAULT_ROW = 7
    DEFAULT_COLUMN = 6
    DEFAULT_CONNECT = 4
    # row
    # column
    # connect
    # active_tokens

    # Constructor taking a row and column
    # @row the number of rows, default DEFAULT_ROW
    # @column the number of columns, default DEFAULT_COLUMN
    # @connect the number to connect
    def __init__(self, row = DEFAULT_ROW, column = DEFAULT_COLUMN, connect = DEFAULT_CONNECT):
        self.row = row
        self.column = column
        self.connect = connect
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
        if self.active_tokens:
            at = self.active_tokens[-1]
            box = [x for x in self.active_tokens if ((x.row > at.row - self.connect and x.column < at.column + self.connect) or \
                (x.row > at.row - self.connect and x.column > at.column - self.connect) or \
                (x.row < at.row + self.connect and x.column < at.column + self.connect) or \
                (x.row < at.row + self.connect and x.column > at.column - self.connect)) and x.player == at.player]

            if self.win_horizontal(box):
                return True
            if self.win_vertical(box):
                return True
            if self.win_diagonal(box):
                return True
        return False

    def win_horizontal(self, box):
        # Getting all tokens from last played Player in same row within the range of the possible win length
        horizontal = [x for x in box if x.row == self.active_tokens[-1].row]
        # Sorting tokens by column
        horizontal.sort(key = lambda x: x.column)
        # Check to see if condition needs to be passed.
        if len(horizontal) < self.connect:
            return False
        # Looping through horizontal tokens and checking for connect
        counter = 1
        for i in range(1, len(horizontal)): 
            # Incrementing counter or resetting
            if horizontal[i].column == horizontal[i - 1].column + 1:
                counter += 1
            else:
                counter = 1
            # If connect then return True
            if counter == self.connect:
                return True
        return False
        
    def win_vertical(self, box):
        # Getting all tokens from last played Player in same column within the range of the possible win length
        vertical = [x for x in box if x.column == self.active_tokens[-1].column]
        # Sorting tokens by row
        vertical.sort(key = lambda x: x.row)
        # Looping through vertical tokens and checking for connect
        if len(vertical) < self.connect:
            return False
        counter = 1
        for i in range(1, len(vertical)):
            # Incrementing counter or resetting
            if vertical[i].row == vertical[i - 1].row + 1:
                counter += 1
            else:
                counter = 1
            # If connect then return True
            if counter == self.connect:
                return True
        return False

    def win_diagonal(self, box):
        # r | c
        # - | +
        # - | -
        # + | +
        # + | - 

        # row - connect <= row <= row + connect


        # all tokens from player within range row and column +- self.connect
        # Take box of certain area. If box isnt a certain size, then dont check this condition. Must have at least self.connect tokens    

        if len(box) < self.connect:
            return False

        # Could maybe just remove the areas of the box that aren't diagnols. 
        # Then specify player and see what exists and try to make a consecutive
        # Diagonal out of it

        # start with count at 0
        # every time we find a token that exists, count += 1
        # if it doesn't exist, set count to 0

        # lower left = token.row - self.connect + 1 and token.column - self.connect + 1
        # lower right = token.row - self.connect + 1 and token.column + self.connect - 1

        # from lower left, add 1 to row and column
        # from lower right, add 1 to row and subtract 1 from column 

        # Lower left calculation
        count = 0
        temp_row = self.active_tokens[-1].row - self.connect + 1
        temp_column = self.active_tokens[-1].column - self.connect + 1
        
        for i in range(2 * self.connect - 1):
            hit = False
            for j in box:
                if j.row == temp_row and j.column == temp_column:
                    hit = True
                    break 
            if hit:
                count += 1
            else:
                count = 0
            if count == self.connect:
                return True
            temp_row += 1
            temp_column += 1

        # Lower Right calculation
        count = 0
        temp_row = self.active_tokens[-1].row - self.connect + 1
        temp_column = self.active_tokens[-1].column + self.connect - 1

        for i in range(2 * self.connect - 1):
            hit = False
            for j in box:
                if j.row == temp_row and j.column == temp_column:
                    hit = True
                    break 
            if hit:
                count += 1
            else:
                count = 0
            if count == self.connect:
                return True
            temp_row += 1
            temp_column -= 1

    # Dunder String method that handles printing the board
    def __str__(self):
        # print out board with tokens
        board = ""
        # Printing board from highest to lowest row
        for i in reversed(range(0,self.row)):
            # Getting only tokens in the current row
            column_data = [x for x in self.active_tokens if x.row == i]
            for j in range(0,self.column):
                # Gets token with matching column and either adds the token or empty
                token = [x for x in column_data if x.column == j]
                if token:
                    board += f"{token[0]} "
                else:
                    board += "_ "
            board += "\n"
        # Adding numbers on bottom
        for i in range(0, self.column):
            board += str(i) + " "
        return board