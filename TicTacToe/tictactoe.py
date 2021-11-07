list_board = list(input("Enter cells: "))
board_1 = list_board.count("X")
board_2 = list_board.count("O")
board_3 = list_board.count("_")
winn = 0


def bard():
    print("-" * 9)
    print(f"""|{list_board[0]} {list_board[1]} {list_board[2]}|
|{list_board[3]} {list_board[4]} {list_board[5]}|
|{list_board[6]} {list_board[7]} {list_board[8]}|""")
    print("-" * 9)


def rslt():
    global winn
    if list_board[0] == list_board[1] == list_board[2] != "_":
        print(list_board[0] + " wins")
        winn += 1
    elif list_board[3] == list_board[4] == list_board[5] != "_":
        print(list_board[3] + " wins")
        winn += 1
    elif list_board[6] == list_board[7] == list_board[8] != "_":
        print(list_board[6] + " wins")
        winn += 1
    elif list_board[2] == list_board[5] == list_board[8] != "_":
        print(list_board[2] + " wins")
        winn += 1
    elif list_board[0] == list_board[3] == list_board[6] != "_":
        print(list_board[0] + " wins")
        winn += 1
    elif list_board[0] == list_board[3] == list_board[6] != "_":
        print(list_board[0] + " wins")
        winn += 1
    elif list_board[1] == list_board[4] == list_board[7] != "_":
        print(list_board[1] + " wins")
        winn += 1
    elif list_board[2] == list_board[5] == list_board[8] != "_":
        print(list_board[2] + " wins")
        winn += 1
    elif board_3 < 1:
        winn += 1
        print("Draw")


bard()
pl = "X"


while True:
    take = input("Enter the coordinates: ")
    coord = list(take)
    x, y = str(coord[2]), str(coord[0])
    if x.isalpha() or y.isalpha() or x == " " or y == " ":
        print("You should enter numbers!")
        continue
    elif y == "1":
        if x == "1":
            if str(list_board[0]) != "X" and list_board[0] != "O":
                list_board[0] = pl
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if list_board[1] != "X" and list_board[1] != "O":
                list_board[1] = pl
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if list_board[2] != "X" and list_board[2] != "O":
                list_board[2] = pl
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "2":
        if x == "1":
            if list_board[3] != "X" and list_board[3] != "O":
                list_board[3] = pl
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if list_board[4] != "X" and list_board[4] != "O":
                list_board[4] = pl
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if list_board[5] != "X" and list_board[5] != "O":
                list_board[5] = pl
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "3":
        if x == "1":
            if list_board[6] != "X" and list_board[6] != "O":
                list_board[6] = pl
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if list_board[7] != "X" and list_board[7] != "O":
                list_board[7] = pl
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if list_board[8] != "X" and list_board[8] != "O":
                list_board[8] = pl
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    else:
        print("Coordinates should be from 1 to 3!")
        continue
    bard()
    rslt()
    if winn > 0:
        break
    if pl == "X":
        pl = "O"
    else:
        pl = "X"
