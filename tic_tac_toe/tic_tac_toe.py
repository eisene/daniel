# print("What's your name?")
# name_1 = input()
# print("Hi " + name_1 + "! Let's play tic tac toe.")

# print("What's the second player's name?")
# name_2 = input()
# print("Hi " + name_2 + "! Let's get started.")


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


test_board_xs = [[0 ,0], [1, 1], [0, 1]]
test_board_os = [[2, 2]]

print_board(test_board_xs, test_board_os)



#     0   1   2
# 0   X | X | 
#    ---+---+---
# 1     | X |   
#    ---+---+---
# 2     |   | O
#