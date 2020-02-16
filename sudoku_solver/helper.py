def in_row(sudoku, row_index, value):
    row = sudoku[row_index]
    return value in row


def in_col(sudoku, col_index, value):
    col = map(lambda x: x[col_index], sudoku)
    return value in col


def mini_grid(sudoku, x, y):
    mini_x = mini_grid_start(x)
    mini_y = mini_grid_start(y)
    return list(map(lambda row: row[mini_x:mini_x+3], sudoku[mini_y: mini_y+3]))


def mini_grid_start(coord):
    if coord in range(3):
        return 0
    if coord in range(6):
        return 3
    if coord in range(9):
        return 6


def in_grid(grid, value):
    found = False
    for row in grid:
        found = value in row
        if found:
            break
    return found


def valid_move(sudoku, x, y, value):
    grid = mini_grid(sudoku, x, y)
    value_in_grid = in_grid(grid, value)
    value_in_row = in_row(sudoku, x, value)
    value_in_col = in_col(sudoku, y, value)
    return not(value_in_col or value_in_row or value_in_grid)
