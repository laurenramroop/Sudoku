import pygame

#finds next row,col on puzzle that isn't filled yet -> -1 = empty cell
def findNextEmpty(puzzle):
    #if none -> return (None, None)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None

#checks if guess at row,col is valid. Returns True if Valid, False if not 
def isValid(puzzle, guess, row, col):
    #checks if guess in row is valid 
    rowVals = puzzle[row]
    if guess in rowVals:
        return False

    #checks if guess in col is valid 
    colVals = []
    for i in range(9):
        colVals.append(puzzle[i][col])
    colVals = [puzzle[i][col] for i in range(9)]
    if guess in colVals:
        return False
    
    #find where 3x3 square starts and iterate over 3 values 
    rowStart = (row // 3) * 3 
    colStart = (col // 3) * 3
    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            if puzzle[r][c] == guess:
                return False 
    
    return True

#backtracking
#board represented by a list of lists, with each inner list representing a row on board
#returns if solution exists
#creates solution with current board if it exists 
def solveSudoku(puzzle):
    #1. find next empty cell
    row, col = findNextEmpty(puzzle)

    if row is None: 
        return True
    
    #2.  If there is a place, make guess 
    for guess in range(1,10):
        #3. Check if valid guess
        if isValid(puzzle, guess, row, col):
            #if valid, then place guess on puzzle
            puzzle[row][col] = guess
            #recursion
            if solveSudoku(puzzle):
                return True
        #backtrack if guess is wrong
        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solveSudoku(example_board))
    print(example_board)
