def is_safe(grid, row, col, num):
    # Check if the number is not repeated in the current row/column/3x3 box
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid, row=0, col=0):
    # If we have reached the last row and last column, return True
    if row == 8 and col == 9:
        return True
    # If we have reached the end of a row, move to the next row and the first column
    if col == 9:
        row += 1
        col = 0
    # If the current position is already filled, move to the next position
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            # Try placing the number in the current cell
            grid[row][col] = num
            # Recursively solve the grid
            if solve_sudoku(grid, row, col + 1):
                return True
        # If the number doesn't work, reset the cell and try again
        grid[row][col] = 0
    return False

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Example Sudoku puzzle (0 represents an empty cell)
sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_puzzle):
    print_grid(sudoku_puzzle)
else:
    print("No solution exists")