# Object for holding token data
class Token:
    # Constructor taking a row, column, and player
    # @row of the Token
    # @column of the Token
    # @player who played the token
    def __init__(self, row, column, player):
        self.row = row
        self.column = column
        self.player = player
        
    # Dunder String method returning the first character of the players name
    def __str__(self):
        return self.player.name[0]