import inspect
import pygame
(width, height) = (300, 200)

class grid:
    title = 'Default Title'

    def __init__(self, title=''):
        self.set_title(title)

    def background_colour(self):
        return (255,255,255)

    def set_title(self, title):
        if len(title) >= 1:
            self.title = title


    def drawgrid(self):
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.title)
        screen.fill(self.background_colour())
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


test = grid('sudoku')
test.drawgrid()