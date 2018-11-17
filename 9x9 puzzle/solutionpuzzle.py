#global variable set to 0

puzzle = 0;

def fill(grid):
    # Look for a unfilled grid location
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                return x, y
    return -1, 1


# This procedure check if setthing the(i,j) squre to a is valid
def isValid(grid, i, j, a):
    rowOk = all([a != grid[i][x] for x in range(9)])
    if rowOk:
        columnok = all([a != grid[x][j] for x in range(9)])
        if columnok:
            # finding the yop left x,y co-ordinates of
            # the section or sub grid containing the i, j cell
            secTopx, secTopy = 3 * (i//3), 3 * (j//3)
            for x in range(secTopx, secTopx + 3):
                for y in range(secTopy, secTopy + 3):
                    if grid[x][y] == a:
                        return False
            return True
    return False

# This procedure fill in the missinf qures of Sudoku

def solveSudoku(grid, i = 0, j = 0):
    
            global puzzle

            # find the next cell to fill
            i, j = fill(grid)
            if i == -1:
                return True

            for e in range(1,10):
                if isValid(grid, i, j, e):
                    grid[i][j] = e
                    if solveSudoku(grid,i,j):
                        return True

                    # Undo Current cell
                    puzzle += 1
                    #puzzle = puzzle + 1
                    grid[i][j] = 0
                    
            return False

def printSudoku(grid):
    numrow = 0
    for row in grid:
        if numrow % 3 == 0 and numrow != 0:
            print(' ')
        print(row[0:3],' ',row[3:6],' ',row[6:9])
        numrow += 1
        #numrow = numrow+1
    return

input = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]


hard = [[8,5,0,0,0,2,4,0,0],
         [7,2,0,0,0,0,0,0,9],
         [0,0,4,0,0,0,0,0,0],
         [0,0,0,1,0,7,0,0,2],
         [3,0,5,0,0,0,9,0,0],
         [0,4,0,0,0,0,0,0,0],
         [0,0,0,0,8,0,0,7,0],
         [0,1,7,0,0,0,0,0,0],
         [0,0,0,0,3,6,0,4,0]]

diffc = [[0,0,5,3,0,0,0,0,0],
         [8,0,0,0,0,0,0,2,0],
         [0,7,0,0,1,0,5,0,0],
         [4,0,0,0,0,5,3,0,0],
         [0,1,0,0,7,0,0,0,6],
         [0,0,3,2,0,0,0,8,0],
         [0,6,0,5,0,0,0,0,9],
         [0,0,4,0,0,0,0,3,0],
         [0,0,0,0,0,9,7,0,0]]

print(solveSudoku(input))
printSudoku(input)
print("Puzzle ",puzzle)


puzzle = 0
printSudoku(hard)
print(solveSudoku(hard))
printSudoku(hard)
print("Puzzle ",puzzle)


puzzle = 0
printSudoku(diffc)
print(solveSudoku(diffc))
printSudoku(diffc)
print("Puzzle ",puzzle) 


            
                
