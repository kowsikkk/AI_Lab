
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def is_valid_move(board, move):
    return move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' '


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


def make_ai_move(board):
    best_score = -float('inf')
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'
    return best_move + 1

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


def main():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O\n")

    print_board(board)

    while True:
        move = input("Enter your move (1-9): ")

        if not is_valid_move(board, move):
            print("Invalid move! Try again.\n")
            continue

        move = int(move) - 1
        board[move] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("You win!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        ai_pos = make_ai_move(board)
        print(f"AI placed O at position {ai_pos}")
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break


# Run program
# if __name__ == "__main__":
main()
