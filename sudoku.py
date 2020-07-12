board = [
# sudoku board. can be changed to any sudoku template

    [7,3,0,4,6,5,0,0,8],
    [0,0,0,3,9,2,4,0,5],
    [5,0,0,0,0,0,0,6,9],
    [0,0,7,0,0,0,8,4,0],
    [0,5,0,8,0,4,0,3,0],
    [0,9,0,2,0,3,0,0,0],
    [2,0,0,0,0,9,1,0,0],
    [9,0,3,5,0,0,7,0,0],
    [0,8,4,7,2,0,0,0,0]
]

def print_board(bo):

# printing board function

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
    # loop for dividing puzzle after 3 rows. to make it more readable

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
        # loop for dividing puzzle after 3 columns. != 0 will not print | on the left side of board. making it more readable

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
            #


def find_empty(bo):
# function for algorithm that finding empty space on board

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)