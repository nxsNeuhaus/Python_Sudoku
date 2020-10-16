import inspect
import pygame

(window_width, window_height) = (725, 700)
grid_width = 630
grid_margin = 5
grid_field = 9

BLACK = (0, 0, 0)
WHITE = (248, 248, 255)
BLUE = (100, 149, 237)


class grid:
    title = 'Default Title'

    def __init__(self, title=''):
        self.set_title(title)

    def set_title(self, title):
        if len(title) >= 1:
            self.title = title

    def window(self):
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(self.title)
        screen.fill(BLACK)
        grid = [
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

        self.drawGrid(grid, screen)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (grid_width + grid_margin)
                    row = pos[1] // (grid_width + grid_margin)

                    print("Click ", pos, "Grid coordinates: ", row, column)

    def drawGrid(self, grid, window):
        for row in range(grid_field):
            for column in range(grid_field):
                color = WHITE
                pygame.draw.rect(
                    window,
                    color,
                    [
                        (grid_margin + grid_width) * column + grid_margin,
                        (grid_margin + grid_width) * row + grid_margin,
                        grid_width,
                        grid_width
                    ]
                )
        return window


test = grid('sudoku')
test.window()
