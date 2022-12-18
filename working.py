import random

board = [                   #example board
    [7,8,0,4,0,0,1,2,0],    #0's count as blanks
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):  # pos --> (row, column)
    #check rows
    for i in range(len(bo[0])):  # iterate through 9 elems in the first
        if bo[pos[0]][i] == num and pos[1] != i:  # check if the row mentioned in the pos tuple and i'th column has the num but
            return False                          # disregarding the position we just entered the num in because its already there

    #check columns
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:     # check if the i'th row and the column mentioned in the pos tuple has the num
            return False                             # but disregarding the position we just entered the num in because its already there

    #check block            (0,0)|(0,1)|(0,2)
    box_x = pos[1] // 3   #------|-----|-------
    box_y = pos[0] // 3   # (1,0)|(1,1)|(1,2)
                          # -----|-----|-------
                          # (2,0)|(2,1)|(2,2)

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo):    # prints the board with lines separating each block and the numbers from the "board" 2D array in their appropriate spots
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")   # horizontal lines after every three rows
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")       # vertical lines after every three columns
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):   # finds empty cells ---> 0 represents empty cell
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)    # (row, column)

    return None

print_board(board)
solve(board)
print("\nBelow is your solved Sudoku puzzle: \n")
print_board(board)