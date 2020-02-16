from . import helper
import numpy as np

sudoku1 = [
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


def solve(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] != 0:
                continue
            for v in range(1, 10):
                if(helper.valid_move(sudoku, x, y, v)):
                    sudoku[y][x] = v
                    if(solve(sudoku)):
                        break
                    sudoku[y][x] = 0
            if sudoku[y][x] == 0:
                return False
    return sudoku


# from sudoku_solver import sudoku_solver
# sudoku_solver.solve(sudoku_solver.sudoku)
