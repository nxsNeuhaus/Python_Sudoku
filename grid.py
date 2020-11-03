import pygame

(window_width, window_height) = (775, 700)
grid_width = 630
grid_margin = 4
grid_field = 9

black = (0, 0, 0)
white = (248, 248, 255)
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
        rectSice = grid_width + grid_margin * grid_field + 1
        pygame.draw.rect(screen, black, [0, 0, rectSice, rectSice])

        for row in range(grid_field):
            for column in range(grid_field):
                color = white

                pygame.draw.rect (
                    screen,
                    color,
                    [
                        (grid_margin + grid_width / grid_field) * column + grid_margin,
                        (grid_margin + grid_width / grid_field) * row + grid_margin,
                        grid_width / grid_field,
                        grid_width / grid_field
                    ]
                )

                if int(grid[row][column]) != 0:
                     myfont = pygame.font.SysFont("times new roman", 64)
                     dicedisplay = myfont.render(str(grid[row][column]), 1, blue)

                     pos1 = (column * (grid_width / grid_field + grid_margin)) + (grid_width / grid_field / 3)
                     pos2 = row * (grid_width / grid_field + grid_margin)
                     screen.blit(dicedisplay, (pos1, pos2))

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (grid_width / grid_field + grid_margin)
                    row = pos[1] // (grid_width / grid_field + grid_margin)

                    print("click ", pos, "grid coordinates: ", row, column)
                    Sudoku.solve()
                    pygame.display.flip()
