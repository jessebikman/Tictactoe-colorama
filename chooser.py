# Allows player to choose their next move
from show import *
def chooser(x_or_o, board):

    while True:
        show(board)
        try:
            x_or_o_input = input("Select a spot[%s]> " % x_or_o)
            x_or_o_input = int(x_or_o_input)
            # Subtract 1 to accomodate for indexing vs regular
            # human sensibility
            x_or_o_input -= 1
            if board[x_or_o_input] == 'x' or board[x_or_o_input] == 'o':
                cleanup()
                print "This spot has already been taken:"
                continue
            else:
                board[x_or_o_input] = x_or_o
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
def _test():
    import doctest
    doctest.testmod()

