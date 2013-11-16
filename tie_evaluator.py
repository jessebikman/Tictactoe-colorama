# Verifies that a tie has taken place
def tie_evaluator(board):

    if board[0] != 1 and board[1] != 2 and board[2] != 3 and \
        board[3] != 4 and board[4] != 5 and board[5] != 6 and \
        board[6] != 7 and board[7] != 8 and board[8] != 9:
        return True
    else:
    	return False

if __name__ == "__main__":
    import doctest
    doctest.testfile("tie_evaluator_tests.txt")
