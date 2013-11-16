#!python2.7
# Author: Jesse Bikman
# This tic-tac-toe game requires the colorama Python library, which is
# available here: http://pypi.python.org/pypi/colorama or can be downloaded
# through pip by typing "sudo pip install colorama" into a terminal window

from tie_evaluator import *
from chooser import *
from victory_evaluator import *
from cleanup import *
init()

# Initializes board
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Keeps the game going until it ends
gameover = False

# Main game loop
while True:
    cleanup()
    chooser('x', board)
    gameover = victory_evaluator(board, 'x')
    if gameover is True:
        print "You won, player who chose 'x'!"
        break
    gameover = tie_evaluator(board)
    if gameover is True:
        print "Cats game!"
        break
    cleanup()
    chooser('o', board)
    gameover = victory_evaluator(board, 'o')
    if gameover is True:
        print "You won, player who chose 'o'!"
        break
        gameover = tie_evaluator(board)
    gameover = tie_evaluator(board)
    if gameover is True:
        print "Cats game!"
        break
