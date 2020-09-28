import inspect
import numpy as np

grid = np.array(
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
    def showgrid(self):
        print(np.matrix(grid))


    def setGrid(self, setGrid):
        global grid
        grid = setGrid


    def possible(self, y, x, n):
        global grid
        for i in range(0, 9):
            if grid[y][i] == n:
                return False
        for i in range(0, 9):
            if grid[i][x] == n:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if grid[y0 + i][x0 + j] == n:
                    return False
        return True


    def solve(self):
        global grid
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1,10):
                        if self.possible(y, x, n):
                            grid[y][x] = n
                            self.solve()
                            # Backtracking
                            grid[y][x] = 0
                    return
        print(np.matrix(grid))