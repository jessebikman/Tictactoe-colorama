# Author: Jesse Bikman

# This tic-tac-toe game requires the colorama Python library, which is
# available here: http://pypi.python.org/pypi/colorama or can be downloaded
# through pip by typing "sudo pip install colorama" into a terminal window

from colorama import init, Fore, Back, Style
import os
init()

# Initializes board
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Prints x's in magenta and o's in green
def colorprint(board, index):
    if board[index] == 'x':
        return Fore.MAGENTA + board[index] + Fore.RESET
    elif board[index] == 'o':
        return Fore.GREEN + board[index] + Fore.RESET
    else:
        return board[index]
# Clears terminal window via os commands, checks operating system to make 
# sure which command is kosher
def cleanup():
    os.system('cls' if os.name=='nt' else 'clear')

# Prints board
def show(board):   
    print colorprint(board, 0), Fore.CYAN + '|' + Fore.RESET, colorprint(board, 1), Fore.CYAN + '|' + Fore.RESET, colorprint(board, 2)
    print Fore.CYAN + '-' * 9 + Fore.RESET
    print colorprint(board, 3), Fore.CYAN + '|' + Fore.RESET, colorprint(board, 4), Fore.CYAN + '|' + Fore.RESET, colorprint(board, 5)
    print Fore.CYAN + '-' * 9 + Fore.RESET
    print colorprint(board, 6), Fore.CYAN + '|' + Fore.RESET, colorprint(board, 7), Fore.CYAN + '|' + Fore.RESET, colorprint(board, 8)

# Allows player to choose their next move
def chooser(x_or_o,board):
    while True:
        show(board)
        try:
            x_or_o_input = input("Select a spot[%s]> " % x_or_o)
            x_or_o_input = int(x_or_o_input)
            if board[x_or_o_input-1] == 'x' or board[x_or_o_input-1] == 'o':
                cleanup()
                print "This spot has already been taken:"
                continue
            else:
                board[x_or_o_input-1] = x_or_o
                break
        except IndexError:
            continue
        except ValueError:
           print("That is not a number on the board.")
           continue
        except TypeError:
           print("That is not a number on the board.")
           continue
        except IndexError:
            print("That is not a number on the board.")
            continue
        except SyntaxError:
            print("That is not a number on the board.")
            continue
        except NameError:
            print("That is not a number on the board.")
            continue

# Checks to see if there's a winner
def victory_evaluator(board,x_or_o):
    if (board[0] == x_or_o and board[1] == x_or_o and board[2] == x_or_o) or (board[3] == x_or_o and board[4] == x_or_o and board[5] == x_or_o) or (board[6] == x_or_o and board[7] == x_or_o and board[8] == x_or_o):
        show(board)
        return True
    elif (board[0] == x_or_o and board[3] == x_or_o and board[6] == x_or_o) or (board[1] == x_or_o and board[4] == x_or_o and board[7] == x_or_o) or (board[2] == x_or_o and board[5] == x_or_o and board[8] == x_or_o):
        show(board)
        return True
    elif (board[0] == x_or_o and board[4] == x_or_o and board[8] == x_or_o) or (board[2] == x_or_o and board[4] == x_or_o and board[6] == x_or_o):
        show(board)
        return True

# Crudely verifies that a tie has taken place
def tie_evaluator(board):
    if(board[0] != 1 and board[1] != 2 and board[2] != 3 and board[3] != 4 and board[4] != 5 and board[5] != 6 and board[6] != 7 and board[7] != 8 and board[8] != 9):
        show(board)
        return True

# Keeps the game going until it ends
gameover = False

# Main game loop
while True:
    cleanup()
    chooser('x',board)
    gameover = victory_evaluator(board, 'x')
    if gameover is True:
        print "You won, player who chose 'x'!"
        break
    gameover = tie_evaluator(board)
    if gameover is True:
        print "Cats game!"
        break
    cleanup()
    chooser('o',board)
    gameover = victory_evaluator(board, 'o')
    if gameover is True:
        print "You won, player who chose 'o'!"
        break
        gameover = tie_evaluator(board)
    gameover = tie_evaluator(board)
    if gameover is True:
        print "Cats game!"
        break
