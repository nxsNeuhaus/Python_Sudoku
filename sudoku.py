from grid import grid

import inspect
import numpy as np

sudokuGrid = np.array(
    [
        [0, 0, 0,   0, 4, 0,   0, 7, 6],
        [7, 1, 0,   3, 9, 0,   0, 0, 0],
        [0, 0, 3,   8, 0, 0,   0, 0, 0],

        [0, 0, 0,   0, 0, 0,   6, 0, 8],
        [3, 0, 4,   0, 0, 0,   7, 0, 5],
        [1, 0, 6,   0, 0, 0,   0, 0, 0],

        [0, 0, 0,   0, 0, 4,   5, 0, 0],
        [0, 0, 0,   0, 7, 5,   0, 9, 1],
        [5, 2, 0,   0, 8, 0,   0, 0, 0]
    ]
)


class Sudoku:
    title = 'sudoku'

    def showgrid(self):
        field = grid('Sudoku')
        # print(np.matrix(sudokuGrid))
        field.window(self)

    def getCurrentGrid(self):
        return sudokuGrid

    def setGrid(self, newGrid):
        global sudokuGrid
        sudokuGrid = newGrid

    def possible(self, y, x, n):
        global sudokuGrid
        for i in range(0, 9):
            if sudokuGrid[y][i] == n:
                return False
        for i in range(0, 9):
            if sudokuGrid[i][x] == n:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if sudokuGrid[y0 + i][x0 + j] == n:
                    return False
        return True

    def solve(self):
        global sudokuGrid
        for y in range(9):
            for x in range(9):
                if sudokuGrid[y][x] == 0:
                    for n in range(1,10):
                        if self.possible(y, x, n):
                            sudokuGrid[y][x] = n
                            self.solve()
                            # Backtracking
                            sudokuGrid[y][x] = 0
                    return
        # print(np.matrix(sudokuGrid))
        self.showgrid()

    def reset(self):
        self.setGrid(np.array(
            [
                [0, 0, 0, 0, 4, 0, 0, 7, 6],
                [7, 1, 0, 3, 9, 0, 0, 0, 0],
                [0, 0, 3, 8, 0, 0, 0, 0, 0],

                [0, 0, 0, 0, 0, 0, 6, 0, 8],
                [3, 0, 4, 0, 0, 0, 7, 0, 5],
                [1, 0, 6, 0, 0, 0, 0, 0, 0],

                [0, 0, 0, 0, 0, 4, 5, 0, 0],
                [0, 0, 0, 0, 7, 5, 0, 9, 1],
                [5, 2, 0, 0, 8, 0, 0, 0, 0]
            ]
        ))
        self.showgrid()
