board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # make an empty board
initialboard = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
x = 0
valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn = 0


def display_board(board):
    print("+------" * 3, "+", sep="")
    for row in range(3):
        print("|      " * 3, "|", sep="")
        for col in range(3):
            print("|  " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|      " * 3, "|", sep="")
        print("+------" * 3, "+", sep="")


def move():
    while 1:
        x = str(input("Please enter your move: "))
        if x in valid:
            return x
        else:
            print("please enter a valid numerical value 1~9: ")
            continue
        break


def puto(x):
    global M
    if x == "1":
        if board[0][0] not in ["X", "O"]:
            board[0][0] = "O"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            puto(M)
    elif x == "2":
        if board[0][1] not in ["X", "O"]:
            board[0][1] = "O"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            puto(M)
    elif x == "3":
        if board[0][2] not in ["X", "O"]:
            board[0][2] = "O"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            puto(M)
    elif x == "4":
        if board[1][0] not in ["X", "O"]:
            board[1][0] = "O"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            puto(M)
    elif x == "5":
        if board[1][1] not in ["X", "O"]:
            board[1][1] = "O"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            puto(M)
    elif x == "6":
        if board[1][2] not in ["X", "O"]:
            board[1][2] = "O"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            puto(M)
    elif x == "7":
        if board[2][0] not in ["X", "O"]:
            board[2][0] = "O"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            puto(M)
    elif x == "8":
        if board[2][1] not in ["X", "O"]:
            board[2][1] = "O"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            puto(M)
    elif x == "9":
        if board[2][2] not in ["X", "O"]:
            board[2][2] = "O"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            puto(M)
    else:
        print(
            """Cell taken!!!
              try another cell"""
        )
        M = move()
        puto(M)


def putx(x):
    global M
    if x == "1":
        if board[0][0] not in ["X", "O"]:
            board[0][0] = "X"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            putx(M)
    elif x == "2":
        if board[0][1] not in ["X", "O"]:
            board[0][1] = "X"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            putx(M)
    elif x == "3":
        if board[0][2] not in ["X", "O"]:
            board[0][2] = "X"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            putx(M)
    elif x == "4":
        if board[1][0] not in ["X", "O"]:
            board[1][0] = "X"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            putx(M)
    elif x == "5":
        if board[1][1] not in ["X", "O"]:
            board[1][1] = "X"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            putx(M)
    elif x == "6":
        if board[1][2] not in ["X", "O"]:
            board[1][2] = "X"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            putx(M)
    elif x == "7":
        if board[2][0] not in ["X", "O"]:
            board[2][0] = "X"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            putx(M)
    elif x == "8":
        if board[2][1] not in ["X", "O"]:
            board[2][1] = "X"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            putx(M)
    elif x == "9":
        if board[2][2] not in ["X", "O"]:
            board[2][2] = "X"
        else:
            print(
                """Cell taken!!!
              try another cell"""
            )
            M = move()
            putx(M)
    else:
        print(
            """Cell taken!!!
              try another cell"""
        )
        M = move()
        putx(M)


def check_x():
    # Check rows
    for row in board:
        if all(cell == "X" for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == "X" for i in range(3)) or all(
        board[i][2 - i] == "X" for i in range(3)
    ):
        return True

    return False


def check_o():
    # Check rows
    for row in board:
        if all(cell == "O" for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == "O" for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == "O" for i in range(3)) or all(
        board[i][2 - i] == "O" for i in range(3)
    ):
        return True

    return False


while turn != 9:
    if check_x() == True:
        print("X wins!!!")
        break

    if check_o() == True:
        print("O wins!!!")
        break

    display_board(board)
    M = move()
    puto(M)
    turn = turn + 1
    display_board(board)
    if turn == 9:
        break
    if check_x() == True:
        print("X wins!!!")
        break

    if check_o() == True:
        print("O wins!!!")
        break
    display_board(board)
    M = move()
    putx(M)
    display_board(board)
    turn = turn + 1


if turn >= 9:
    print("Game over")
