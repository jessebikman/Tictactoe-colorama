from colorama import init, Fore, Back, Style

# Prints board
def show(board):

    print colorprint(board, 0), Fore.CYAN + '|' + Fore.RESET, \
        colorprint(board, 1), Fore.CYAN + '|' + Fore.RESET, \
        colorprint(board, 2)
    print Fore.CYAN + '-' * 9 + Fore.RESET
    print colorprint(board, 3), Fore.CYAN + '|' + Fore.RESET, \
        colorprint(board, 4), Fore.CYAN + '|' + Fore.RESET, \
        colorprint(board, 5)
    print Fore.CYAN + '-' * 9 + Fore.RESET
    print colorprint(board, 6), Fore.CYAN + '|' + Fore.RESET, \
        colorprint(board, 7), Fore.CYAN + '|' + Fore.RESET, \
        colorprint(board, 8)

# Prints x's in magenta and o's in green
def colorprint(board, index):
    if board[index] == 'x':
        return Fore.MAGENTA + board[index] + Fore.RESET
    elif board[index] == 'o':
        return Fore.GREEN + board[index] + Fore.RESET
    else:
        return board[index]

