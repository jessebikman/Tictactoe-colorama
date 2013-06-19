# Author: Jesse Bikman

# This tic-tac-toe game requires the colorama Python library, which is
# available here: http://pypi.python.org/pypi/colorama or can be downloaded
# through pip by typing "sudo pip install colorama" into a terminal window

from colorama import init, Fore, Back, Style
import os
init()

# Initializes board
board1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board2 = [10, 11, 12, 13, 14, 15, 16, 17, 18]
board3 = [19, 20, 21, 22, 23, 24, 25, 26, 27]
board4 = [28, 29, 30, 31, 32, 33, 34, 35, 36]
board5 = [37, 38, 39, 40, 41, 42, 43, 44, 45]
board6 = [46, 47, 48, 49, 50, 51, 52, 53, 54]
board7 = [55, 56, 57, 58, 59, 60, 61, 62, 63]
board8 = [64, 65, 66, 67, 68, 69, 70, 71, 72]
board9 = [73, 74, 75, 76, 77, 78, 79, 80, 81]

boardboard = [board1, board2, board3, board4, board5, board6, board7, board8, board9]


# Prints x's in magenta and o's in green
def colorprint(boardboard, index):
    if boardboard[index] == 'x':
        return Fore.MAGENTA + boardboard[index] + Fore.RESET
    elif boardboard[index] == 'o':
        return Fore.GREEN + boardboard[index] + Fore.RESET
    else:
        return boardboard[index]


# Clears terminal window via os commands, checks operating system to make
# sure which command is kosher
def cleanup():

    os.system('cls' if os.name == 'nt' else 'clear')


# Prints board
def show(boardboard):
    
        print Fore.CYAN + '|' * 56 + Fore.RESET
        print Fore.CYAN + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + Fore.RESET  
        print Fore.CYAN + '|| ' + Fore.RESET, \
            colorprint(boardboard[0], 0), Fore.CYAN + ' |' + Fore.RESET, \
            colorprint(boardboard[0], 1), Fore.CYAN + ' |' + Fore.RESET, \
            colorprint(boardboard[0], 2), Fore.CYAN + '  || ' + Fore.RESET, \
            colorprint(boardboard[1], 0), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[1], 1), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[1], 2), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[2], 0), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[2], 1), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[2], 2), Fore.CYAN + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + '-' * 14 + ' || ' + '-' * 14 + ' || ' + '-' * 14 + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + Fore.RESET, \
            colorprint(boardboard[0], 3), Fore.CYAN + ' |' + Fore.RESET, \
            colorprint(boardboard[0], 4), Fore.CYAN + ' |' + Fore.RESET, \
            colorprint(boardboard[0], 5), Fore.CYAN + '  || ' + Fore.RESET, \
            colorprint(boardboard[1], 3), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[1], 4), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[1], 5), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[2], 3), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[2], 4), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[2], 5), Fore.CYAN + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + '-' * 14 + ' || ' + '-' * 14 + ' || ' + '-' * 14 + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + Fore.RESET, \
            colorprint(boardboard[0], 6), Fore.CYAN + ' |' + Fore.RESET, \
            colorprint(boardboard[0], 7), Fore.CYAN + ' |' + Fore.RESET, \
            colorprint(boardboard[0], 8), Fore.CYAN + '  || ' + Fore.RESET, \
            colorprint(boardboard[1], 6), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[1], 7), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[1], 8), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[2], 6), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[2], 7), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[2], 8), Fore.CYAN + ' ||' + Fore.RESET
        print Fore.CYAN + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + Fore.RESET  
        print Fore.CYAN + '|' * 56 + Fore.RESET
        print Fore.CYAN + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + Fore.RESET  
        print Fore.CYAN + '|| ' + Fore.RESET, \
            colorprint(boardboard[3], 0), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[3], 1), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[3], 2), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[4], 0), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[4], 1), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[4], 2), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[5], 0), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[5], 1), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[5], 2), Fore.CYAN + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + '-' * 14 + ' || ' + '-' * 14 + ' || ' + '-' * 14 + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + Fore.RESET, \
            colorprint(boardboard[3], 3), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[3], 4), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[3], 5), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[4], 3), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[4], 4), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[4], 5), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[5], 3), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[5], 4), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[5], 5), Fore.CYAN + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + '-' * 14 + ' || ' + '-' * 14 + ' || ' + '-' * 14 + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + Fore.RESET, \
            colorprint(boardboard[3], 6), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[3], 7), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[3], 8), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[4], 6), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[4], 7), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[4], 8), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[5], 6), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[5], 7), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[5], 8), Fore.CYAN + ' ||' + Fore.RESET
        print Fore.CYAN + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + Fore.RESET  
        print Fore.CYAN + '|' * 56 + Fore.RESET
        print Fore.CYAN + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + Fore.RESET  
        print Fore.CYAN + '|| ' + Fore.RESET, \
            colorprint(boardboard[6], 0), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[6], 1), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[6], 2), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[7], 0), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[7], 1), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[7], 2), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[8], 0), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[8], 1), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[8], 2), Fore.CYAN + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + '-' * 14 + ' || ' + '-' * 14 + ' || ' + '-' * 14 + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + Fore.RESET, \
            colorprint(boardboard[6], 3), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[6], 4), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[6], 5), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[7], 3), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[7], 4), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[7], 5), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[8], 3), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[8], 4), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[8], 5), Fore.CYAN + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + '-' * 14 + ' || ' + '-' * 14 + ' || ' + '-' * 14 + ' ||' + Fore.RESET
        print Fore.CYAN + '|| ' + Fore.RESET, \
            colorprint(boardboard[6], 6), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[6], 7), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[6], 8), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[7], 6), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[7], 7), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[7], 8), Fore.CYAN + ' || ' + Fore.RESET, \
            colorprint(boardboard[8], 6), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[8], 7), Fore.CYAN + '|' + Fore.RESET, \
            colorprint(boardboard[8], 8), Fore.CYAN + ' ||' + Fore.RESET
        print Fore.CYAN + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + ' ' * 16 + '||' + Fore.RESET  
        print Fore.CYAN + '|' * 56 + Fore.RESET



        # print colorprint(boardboard, 3), Fore.CYAN + '|' + Fore.RESET, \
        #     colorprint(boardboard, 4), Fore.CYAN + '|' + Fore.RESET, \
        #     colorprint(boardboard, 5)
        # print Fore.CYAN + '-' * 9 + Fore.RESET
        # print colorprint(boardboard, 6), Fore.CYAN + '|' + Fore.RESET, \
        #     colorprint(boardboard, 7), Fore.CYAN + '|' + Fore.RESET, \
        #     colorprint(boardboard, 8)


# Allows player to choose their next move
def chooser(x_or_o, boardboard):

    while True:
        show(boardboard)
        try:
            x_or_o_input = input("Select a spot[%s]> " % x_or_o)
            x_or_o_input = int(x_or_o_input)
            # Subtract 1 to accomodate for indexing vs regular
            # human sensibility
            x_or_o_input -= 1
            if boardboard[x_or_o_input] == 'x' or boardboard[x_or_o_input] == 'o':
                cleanup()
                print "This spot has already been taken:"
                continue
            else:
                boardboard[x_or_o_input] = x_or_o
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
def victory_evaluator(board, x_or_o):

    if board[0] == x_or_o and board[1] == x_or_o and board[2] == x_or_o or \
        board[3] == x_or_o and board[4] == x_or_o and board[5] == x_or_o or \
        board[6] == x_or_o and board[7] == x_or_o and board[8] == x_or_o:
        show(boardboard)
        return True
    elif board[0] == x_or_o and board[3] == x_or_o and board[6] == x_or_o or \
        board[1] == x_or_o and board[4] == x_or_o and board[7] == x_or_o or \
        board[2] == x_or_o and board[5] == x_or_o and board[8] == x_or_o:
        show(boardboard)
        return True
    elif board[0] == x_or_o and board[4] == x_or_o and board[8] == x_or_o or \
        board[2] == x_or_o and board[4] == x_or_o and board[6] == x_or_o:
        show(boardboard)
        return True


# Crudely verifies that a tie has taken place
def tie_evaluator(board):

    if board[0] != 1 and board[1] != 2 and board[2] != 3 and \
        board[3] != 4 and board[4] != 5 and board[5] != 6 and \
        board[6] != 7 and board[7] != 8 and board[8] != 9:
        show(boardboard)
        return True

# Keeps the game going until it ends
gameover = False

# Main game loop
while True:
    cleanup()
    chooser('x', boardboard)
    gameover = victory_evaluator(boardboard, 'x')
    if gameover is True:
        print "You won, player who chose 'x'!"
        break
    gameover = tie_evaluator(boardboard)
    if gameover is True:
        print "Cats game!"
        break
    cleanup()
    chooser('o', boardboard)
    gameover = victory_evaluator(boardboard, 'o')
    if gameover is True:
        print "You won, player who chose 'o'!"
        break
        gameover = tie_evaluator(boardboard)
    gameover = tie_evaluator(boardboard)
    if gameover is True:
        print "Cats game!"
        break
