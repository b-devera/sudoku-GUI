board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Returns an empty tile on the sudoku board
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Prints the sudoku board
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")

# Checks if the given number does not exist in the row, column, or box that the number is placed at
def isValid(board, number, position):
    # Check row
    for i in range(0, len(board)):
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    # Check column
    for j in range(0, len(board)):
        if board[j][position[1]] == number and position[1] != j:
            return False

    # Check box
    box_X = position[1] // 3
    box_Y = position[0] // 3

    for i in range(box_Y*3, box_Y*3 + 3):
        for j in range(box_X*3, box_X*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    
    # If none of these conditions are valid, then the number is valid
    return True

# Solves the sudoku board
def solve(board):
    search = findEmpty(board)
    if not search:
        return True
    else:
        i, j = search

    for number in range(1,10):
        if isValid(board, number, (i, j)):
            board[i][j] = number

            if solve(board):
                return True
            
            board[i][j] = 0
    
    return False

print("Unsolved:")
printBoard(board)
solve(board)
print("\nSolved:")
printBoard(board)