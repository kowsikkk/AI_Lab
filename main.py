def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("--|---|--")
    print()

def is_valid(board,move):
    return move.isdigit() and 1 <= int(move) <=9 and board[int(move)-1]==' '

def check_win(board,player):
    win_condition = [
        (1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)
    ]
    for i,j,k in win_condition:
        if board[i-1]==board[j-1]==board[k-1]==player:
            return True
    return False

def is_draw(board):
    return ' ' not in board

def make_ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            score=minmax(board,False)
            board[i]=' '
            if score>best_score:
                best_score=score
                best_move=i
    board[best_move]='O'
    return best_move + 1

def minmax(board,player):
    if check_win(board,'O'):
        return 1
    if check_win(board,'X'):
        return -1
    if is_draw(board):
        return 0

    if player:
        best=-float('inf')
        for i in range(9):
            if board[i]==' ':
                board[i]='O'
                best=max(best,minmax(board,False))
                board[i]=' '
        return best
    else:
        best=float('inf')
        for i in range(9):
            if board[i]==' ':
                board[i]='X'
                best=min(best,minmax(board,True))
                board[i]=' '
        return best

def main():
    board=[' ']*9
    print_board(board)
    while True:
        move=input("Enter the number 1-9 :")

        if not is_valid(board,move):
            print("Invalid Move")
            continue

        move = int(move) - 1
        board[move]='X'
        print_board(board)

        if check_win(board,'X'):
            print("You Win")
            break
        if is_draw(board):
            print("Draw")
            break

        pos=make_ai_move(board)
        print("the ai position is :",pos)
        print_board(board)

        if check_win(board,'O'):
            print("You Lose")
            break
        if is_draw(board):
            print("Draw")
            break

main()
