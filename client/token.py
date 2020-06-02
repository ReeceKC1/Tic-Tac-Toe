class Token:
    def __init__(self, row, column, player):
        self.row = row
        self.column = column
        self.player = player
        
    def __str__(self):
        return self.player.name[0]