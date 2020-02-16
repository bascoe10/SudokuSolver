import pytest
from .context import sudoku_solver
from sudoku_solver.helper import in_row, in_col, mini_grid_start, mini_grid, in_grid, valid_move


class TestSudokuSolverHelper():

    @pytest.fixture(autouse=True)
    def sudoku(self):
        return(
            [
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
        )

    @pytest.fixture
    def mini_grid_start_map(self):
        return({
            0: 0, 1: 0, 2: 0, 3: 3, 4: 3, 5: 3, 6: 6, 7: 6, 8: 6
        })

    def test_in_row(self, sudoku):
        assert in_row(sudoku, 0, 5)

    def test_not_in_row(self, sudoku):
        assert in_row(sudoku, 0, 9) == False

    def test_in_col(self, sudoku):
        assert in_col(sudoku, 0, 8)

    def test_not_in_col(self, sudoku):
        assert in_col(sudoku, 0, 9) == False

    def test_mini_grid_start(self, mini_grid_start_map):
        for i in range(9):
            assert mini_grid_start_map[i] == mini_grid_start(i)

    def test_mini_grid(self, sudoku):
        assert mini_grid(sudoku, 1, 1) == [
            [5, 3, 0],
            [6, 0, 0],
            [0, 9, 8]
        ]

    def test_in_grid(self, sudoku):
        grid = mini_grid(sudoku, 1, 1)
        assert in_grid(grid, 9)

    def test_not_in_grid(self, sudoku):
        grid = mini_grid(sudoku, 1, 1)
        assert in_grid(grid, 1) == False

    def test_valid_move(self, sudoku):
        assert valid_move(sudoku, 1, 2, 7)

    def test_not_valid_move_because_row(self, sudoku):
        assert valid_move(sudoku, 1, 2, 1) == False

    def test_not_valid_move_because_col(self, sudoku):
        assert valid_move(sudoku, 1, 2, 3) == False

    def test_not_valid_move_because_grid(self, sudoku):
        assert valid_move(sudoku, 1, 2, 5) == False
