from show import *
# Checks to see if there's a winner
def victory_evaluator(board, x_or_o):

    if board[0] == x_or_o and board[1] == x_or_o and board[2] == x_or_o or \
        board[3] == x_or_o and board[4] == x_or_o and board[5] == x_or_o or \
        board[6] == x_or_o and board[7] == x_or_o and board[8] == x_or_o:
        show(board)
        return True
    elif board[0] == x_or_o and board[3] == x_or_o and board[6] == x_or_o or \
        board[1] == x_or_o and board[4] == x_or_o and board[7] == x_or_o or \
        board[2] == x_or_o and board[5] == x_or_o and board[8] == x_or_o:
        show(board)
        return True
    elif board[0] == x_or_o and board[4] == x_or_o and board[8] == x_or_o or \
        board[2] == x_or_o and board[4] == x_or_o and board[6] == x_or_o:
        show(board)
        return True
