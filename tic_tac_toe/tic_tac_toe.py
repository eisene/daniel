def print_board_square(board_xs, board_os, square_coord):
    print("+---+")
    if square_coord in board_xs:
        print("| X |")
    elif square_coord in board_os:
        print("| O |")
    else:
        print("|   |")
    print("+---+")


def print_board_row(board_xs, board_os, row_index):
    if row_index == 0:
        print("+---+---+---+")

    if [row_index, 0] in board_xs:
        first_position = "X"
    elif [row_index, 0] in board_os:
        first_position = "O"
    else:
        first_position = " "

    if [row_index, 1] in board_xs:
        second_position = "X"
    elif [row_index, 1] in board_os:
        second_position = "O"
    else:
        second_position = " "

    if [row_index, 2] in board_xs:
        third_position = "X"
    elif [row_index, 2] in board_os:
        third_position = "O"
    else:
        third_position = " "

    print("| " + first_position + " | " + second_position + " | " + third_position + " |")

    print("+---+---+---+")


def print_board(board_xs, board_os):
    for row in range(3):
        print_board_row(board_xs, board_os, row)


print("What's your name?")
name_1 = input()
print("Hi " + name_1 + "! Let's play tic tac toe. You will be Xs.")

print()
print("What's the second player's name?")
name_2 = input()
print("Hi " + name_2 + "! Let's get started. You will be Os.")

board_xs = []
board_os = []
while True:
    print()
    print("It's your turn " + name_1 + "! You are Xs.")

    while True:
        while True:
            print("What row do you want to put your X in?")
            row = int(input()) - 1
            if row < 0 or row > 2:
                print("Enter a row between 1 and 3!!!")
                continue
            break

        while True:
            print("What column do you want to put your X in?")
            column = int(input()) - 1
            if column < 0 or column > 2:
                print("Enter a column between 1 and 3!!!")
                continue
            break

        # Check if this spot is NOT full
        if not ([row, column] in board_xs or [row, column] in board_os):
            # If NOT full, break the loop
            break
        # If full, repeat and ask again
        print("THIS SPOT IS FULL!!!! Enter a different spot!")

    board_xs.append([row, column])
    print_board(board_xs, board_os)

    # Check if anyone won
    someone_won = False
    for row in range(2):
        if [row, 0] in board_xs and [row, 1] in board_xs and [row, 2] in board_xs:
            print("Xs WIN!!!")
            someone_won = True
        if [row, 0] in board_os and [row, 1] in board_os and [row, 2] in board_os:
            print("Os WIN!!!")
            someone_won = True
    for column in range(2):
        if [0, column] in board_xs and [1, column] in board_xs and [2, column] in board_xs:
            print("Xs WIN!!!")
            someone_won = True
        if [0, column] in board_os and [1, column] in board_os and [2, column] in board_os:
            print("Os WIN!!!")
            someone_won = True
    if [0, 0] in board_xs and [1, 1] in board_xs and [2, 2] in board_xs:
        print("Xs WIN!!!")
        someone_won = True
    if [0, 0] in board_os and [1, 1] in board_os and [2, 2] in board_os:
        print("Os WIN!!!")
        someone_won = True
    if [0, 2] in board_xs and [1, 1] in board_xs and [2, 0] in board_xs:
        print("Xs WIN!!!")
        someone_won = True
    if [0, 2] in board_os and [1, 1] in board_os and [2, 0] in board_os:
        print("Os WIN!!!")
        someone_won = True
    if someone_won:
        break

    print()
    print("It's your turn " + name_2 + "! You are Os.")

    while True:
        while True:
            print("What row do you want to put your O in?")
            row = int(input()) - 1
            if row < 0 or row > 2:
                print("Enter a row between 1 and 3!!!")
                continue
            break

        while True:
            print("What column do you want to put your O in?")
            column = int(input()) - 1
            if column < 0 or column > 2:
                print("Enter a column between 1 and 3!!!")
                continue
            break

        # Check if this spot is NOT full
        if not ([row, column] in board_xs or [row, column] in board_os):
            # If NOT full, break the loop
            break
        # If full, repeat and ask again
        print("THIS SPOT IS FULL!!!! Enter a different spot!")

    board_os.append([row, column])
    print_board(board_xs, board_os)

    # Check if anyone won
    someone_won = False
    for row in range(2):
        if [row, 0] in board_xs and [row, 1] in board_xs and [row, 2] in board_xs:
            print("Xs WIN!!!")
            someone_won = True
        if [row, 0] in board_os and [row, 1] in board_os and [row, 2] in board_os:
            print("Os WIN!!!")
            someone_won = True
    for column in range(2):
        if [0, column] in board_xs and [1, column] in board_xs and [2, column] in board_xs:
            print("Xs WIN!!!")
            someone_won = True
        if [0, column] in board_os and [1, column] in board_os and [2, column] in board_os:
            print("Os WIN!!!")
            someone_won = True
    if [0, 0] in board_xs and [1, 1] in board_xs and [2, 2] in board_xs:
        print("Xs WIN!!!")
        someone_won = True
    if [0, 0] in board_os and [1, 1] in board_os and [2, 2] in board_os:
        print("Os WIN!!!")
        someone_won = True
    if [0, 2] in board_xs and [1, 1] in board_xs and [2, 0] in board_xs:
        print("Xs WIN!!!")
        someone_won = True
    if [0, 2] in board_os and [1, 1] in board_os and [2, 0] in board_os:
        print("Os WIN!!!")
        someone_won = True
    if someone_won:
        break

    # Check if the board is full - check if there are exactly 9 Xs and Os in total?
    number_of_xs = len(board_xs)
    number_of_os = len(board_os)
    if number_of_xs + number_of_os == 9:
        print("Game over!")
        break


# test_board_xs = [[0 ,0], [1, 1], [0, 1]]
# test_board_os = [[2, 2]]

# print_board(test_board_xs, test_board_os)



#     0   1   2
# 0     |   | x
#    ---+---+---
# 1     | x |   
#    ---+---+---
# 2   x |   |  
#


# ROW:    [1, 0], [1, 1], [1, 2]
# COLUMN: [0, 1], [1, 1], [2, 1]