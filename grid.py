import pygame
import copy

(window_width, window_height) = (660, 660)
grid_width = 630
grid_margin = 2
grid_field = 9

black = (0, 0, 0)
white = (255, 255, 255)
gray = (237, 237, 237)
blue = (100, 149, 237)


class grid:
    title = 'default title'

    def __init__(self, title=''):
        self.set_title(title)
        pygame.init()

    def set_title(self, title):
        if len(title) >= 1:
            self.title = title

    def window(self, Sudoku):
        grid = Sudoku.getCurrentGrid()
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(self.title)

        screen.fill(white)
        rectSice = grid_width + grid_margin * grid_field + 6

        pygame.draw.rect(screen, black, [3, 3, rectSice, rectSice])

        for row in range(grid_field):
            for column in range(grid_field):
                if (row in (0, 1, 2, 6, 7, 8) and column in (0, 1, 2, 6, 7, 8)) or (row in (3, 4, 5) and column in (3, 4, 5)):
                    margin = copy.deepcopy(grid_margin)
                    self.drawRect(column, row, screen, gray, margin)
                else:
                    margin = copy.deepcopy(grid_margin)
                    self.drawRect(column, row, screen, white, margin)

                if int(grid[row][column]) != 0:
                    myfont = pygame.font.SysFont("times new roman", 64)
                    dicedisplay = myfont.render(str(grid[row][column]), 1, blue)

                    pos1 = (column * (grid_width / grid_field + grid_margin)) + (grid_width / grid_field / 3) + 5
                    pos2 = row * (grid_width / grid_field + grid_margin) + 5
                    screen.blit(dicedisplay, (pos1, pos2))

        pygame.draw.line(screen, black, (220, 5), (220, 655))
        pygame.draw.line(screen, black, (223, 5), (223, 655))

        pygame.draw.line(screen, black, (436, 5), (436, 655))
        pygame.draw.line(screen, black, (439, 5), (439, 655))

        pygame.draw.line(screen, black, (5, 220), (655, 220))
        pygame.draw.line(screen, black, (5, 222), (655, 222))

        pygame.draw.line(screen, black, (5, 437), (655, 437))
        pygame.draw.line(screen, black, (5, 439), (655, 439))

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    column, row = self.getGridPosFromMousePos()
                elif event.type == pygame.KEYUP:
                    if (event.key == pygame.K_1 or event.key == pygame.K_KP1):
                        self.updateFieldInput(Sudoku, grid, 1)
                    elif (event.key == pygame.K_2 or event.key == pygame.K_KP2):
                        self.updateFieldInput(Sudoku, grid, 2)
                    elif (event.key == pygame.K_3 or event.key == pygame.K_KP3):
                        self.updateFieldInput(Sudoku, grid, 3)
                    elif (event.key == pygame.K_4 or event.key == pygame.K_KP4):
                        self.updateFieldInput(Sudoku, grid, 4)
                    elif (event.key == pygame.K_5 or event.key == pygame.K_KP5):
                        self.updateFieldInput(Sudoku, grid, 5)
                    elif (event.key == pygame.K_6 or event.key == pygame.K_KP6):
                        self.updateFieldInput(Sudoku, grid, 6)
                    elif (event.key == pygame.K_7 or event.key == pygame.K_KP7):
                        self.updateFieldInput(Sudoku, grid, 7)
                    elif (event.key == pygame.K_8 or event.key == pygame.K_KP8):
                        self.updateFieldInput(Sudoku, grid, 8)
                    elif (event.key == pygame.K_9 or event.key == pygame.K_KP9):
                        self.updateFieldInput(Sudoku, grid, 9)
                    elif (event.key == pygame.K_0 or event.key == pygame.K_DELETE or event.key == pygame.K_KP0):
                        self.updateFieldInput(Sudoku, grid, 0)
                    elif (event.key == pygame.K_F1):
                        Sudoku.solve()
                    elif (event.key == pygame.K_F2):
                        Sudoku.reset()
                    elif (event.key == pygame.K_F3):
                        Sudoku.getRandomGrid()

    def drawRect(self, column, row, screen, color, margin):
        pygame.draw.rect(
            screen,
            color,
            [
                (margin + grid_width / grid_field) * column + margin + 5,
                (margin + grid_width / grid_field) * row + margin + 5,
                grid_width / grid_field,
                grid_width / grid_field
            ]
        )

    def updateFieldInput(self, Sudoku, grid, numberValue):
        column, row = self.getGridPosFromMousePos()
        try:
            grid[row][column] = int(numberValue)
            Sudoku.setGrid(grid)
            Sudoku.showgrid()
            pygame.display.flip()
        except IndexError:
            pass

    def getGridPosFromMousePos(self):
        pos = pygame.mouse.get_pos()
        column = pos[0] // (grid_width / grid_field + grid_margin)
        row = pos[1] // (grid_width / grid_field + grid_margin)
        print(pos, column, row)
        return int(column), int(row)
