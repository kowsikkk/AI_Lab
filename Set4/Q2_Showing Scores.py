def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    for i, j, k in win_conditions:
        if board[i] == board[j] == board[k] == player:
            return True
    return False


def is_draw(board):
    return ' ' not in board


def minimax(board, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(board, False))
                board[i] = ' '
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(board, True))
                board[i] = ' '
        return best



board = [' ', 'X', 'O', ' ', ' ', 'X', ' ', 'O', ' ']  # Example state

print("\nPossible moves and minimax scores:")
for i in range(9):
    if board[i] == ' ':
        board[i] = 'O'
        score = minimax(board, False)
        board[i] = ' '
        print(f"Move {i+1}: Score = {score}")
