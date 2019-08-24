from copy import deepcopy


def main():

    board = [0, 1, 2], [0, 1, 2], [0, 1, 2]
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = 0

    print_board(board)

    while check_full_board(board):
        while True:
            row = input("Enter Row(0,1,2)")  # ("Enter an X: (row, column) ")
            column = input("Enter Column (0,1,2")
            r = int(row)
            c = int(column)
            if board[r][c] == 0:
                board[r][c] = "X"
                break
            else:
                print("Invalid, try again")
        if check_win(board):
            print("X wins")
            break
        #Computers Turn as Y
        if check_full_board(board)is False: #Updates check_full_board
            break
        board = computer_ai(board)
        print_board(board)
        if check_win(board):
            print("O Wins")
            break
    print("Tie")


def print_board(board):
    for i in range(len(board)):
        print(board[i])


def computer_ai(board):
    for i in range(len(board)): #1 Win, if making a move wins the game, make the move
        for j in range(len(board[i])):
            if board[i][j] == 0:
                board2 = deepcopy(board)
                board2[i][j] = "O"
                if check_win(board2):
                    return board2

    for i in range(len(board)):  # 2 Block, if making a move results for X results in a win, block it
        for j in range(len(board[i])):
            if board[i][j] == 0:
                board2 = deepcopy(board)
                board2[i][j] = "X"
                if check_win(board2):
                    board[i][j] = "O"
                    return board

    for i in range(len(board)): #3 Create a fork, or two places to win
        for j in range(len(board[i])):
            if board[i][j] == 0: #Runs 5 times
                board3 = deepcopy(board) #run the win function on board 3, if that returns true, set board [i][j] = 'O' and return the board
                board3[i][j] = "O"

                if check_for_fork(board3, "O"):
                    board[i][j] = 'O'
                    print("CPU creates a Fork")
                    return board

    #Check to see if first move was corner before blocking fork, SPECIAL CASE
    # if x is in opposite corners and o is in the center and the rest of the board is empty, play an edge
    if board[0][0] == "X" and board[2][2] == "X" and board[1][1] == "O":
        if board[0][1] == 0:
            board[0][1] = "O"
            return board
        elif board[1][0] == 0:
            board[1][0] = "O"
            return board
        elif board[1][2] == 0:
            board[1][2] = "O"
            return board
        elif board[2][1] == 0:
            board[2][1] = "O"
            return board
    if board[0][2] == "X" and board[2][0] and board[1][1] == "O":
        if board[0][1] == 0:
            board[0][1] = "O"
            return board
        elif board[1][0] == 0:
            board[1][0] = "O"
            return board
        elif board[1][2] == 0:
            board[1][2] = "O"
            return board
        elif board[2][1] == 0:
            board[2][1] = "O"
            return board
    for i in range(len(board)):  #4 Block an opponents fork
        for j in range(len(board[i])):
            if board[i][j] == 0:  # Runs 5 times
                board3 = deepcopy(board)
                board3[i][j] = "X"

                if check_for_fork(board3, "X"):
                    board[i][j] = 'O'
                    print("CPU Blocks a Fork")
                    return board

    if board[1][1] == 0: #5 Player marks the center if available
        board[1][1] = "O"
        return board

    if opposite_corner(board): #6 Oppsite Corner
        return board

    if empty_corner(board): #7 Empty Corner
        return board

    if empty_side(board): #8 empty side
        return board


def check_for_fork(board3, x_or_o):
    counter = 0
    for i in range(len(board3)):  # 1 Win, if making a move wins the game, make the move
        for j in range(len(board3[i])):
            if board3[i][j] == 0:
                board4 = deepcopy(board3)
                board4[i][j] = x_or_o

                if check_row(board4):
                    counter+=1
                if check_diagonal(board4):
                    counter+=1
                if check_column(board4):
                    counter+=1

            if counter >=2:
                return True

    return False


def empty_corner(board):
    if board[0][0] == 0:
        board[0][0] = "O"
        return True
    elif board[0][2] == 0:
        board[0][2] = "O"
        return True
    elif board[2][0] == 0:
        board[2][0] = "O"
        return True
    elif board[2][2] == 0:
        board[2][2] = "O"
        return True
    return False


def opposite_corner(board):
    if board[0][0] == "X":
        if board[2][2] == 0:
            board[2][2] = "O"
            return True
    elif board[0][2] == "X":
        if board[2][0] == 0:
            board[2][0] = "O"
            return True
    elif board[2][0] == "X":
        if board[0][2] == 0:
            board[0][2] = "O"
            return True
    elif board[2][2] == "X":
        if board[0][0] == 0:
            board[0][0] = "O"
            return True
    return False


def empty_side(board):
    if board[0][1] == 0:
        board[0][1] = "O"
        return True
    elif board[1][0] == 0:
        board[1][0] = "O"
        return True
    elif board[1][2] == 0:
        board[1][0] = "O"
        return True
    elif board[2][1] == 0:
        board[2][1] = "O"
        return True
    return False


def check_row(board):
    if board[0][0] != 0 and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return True
    if board[1][0] != 0 and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return True
    if board[2][0] != 0 and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return True
    return False


def check_diagonal(board):
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    if board[0][2] != 0 and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True
    return False


def check_column(board):
    if board[0][0] != 0 and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return True
    if board[0][1] != 0 and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return True
    if board[0][2] != 0 and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return True
    return False


def check_win(board):
    #Diagonal
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    if board[0][2] != 0 and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True
    #Row
    if board[0][0] != 0 and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return True
    if board[1][0] != 0 and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return True
    if board[2][0] != 0 and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return True
    #Column
    if board[0][0] != 0 and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return True
    if board[0][1] != 0 and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return True
    if board[0][2] != 0 and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return True
    return False


def check_full_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return True
    return False


def check_perfect_player(board):
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            counter += 1

    print(counter)


main()
