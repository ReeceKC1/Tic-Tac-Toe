from client.game import Game
from objects.player import *


player1 = LocalPlayer()
player1.name = "Jeff"

player2 = LocalPlayer()
player2.name = "Omar"


game = Game(player1, player2)

game.start()