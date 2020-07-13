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

def solve(bo):
    # finding empty spaces. if they have not been found it will return True

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        # looping with numbers from 1 to 9. If loop through whole range and does not find solution return false and backtrack.
        # If after looping will find some number, will write it to the free box
        if validating(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def validating(bo, numb, pos):
    # function checking rows, columns and little squares

    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == numb and pos[1] != i: # pos[0][i] -> rows, col
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == numb and pos[0] != i:
            return False

    # check little square
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_x * 3 + 3):
        for j in range(box_x * 3, box_y * 3 + 3):
            if bo[i][j] == numb and (i, j) != pos:
                return False

    return True


def print_board(bo):

# printing board function

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
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
solve(board)
print('-----------------------')
print_board(board)