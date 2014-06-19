import pygame

class Cell(object):

    def __init__(self, x, y):

        super(Cell, self).__init__()

        self.rect = pygame.rect.Rect(x, y, 6, 6)
        self.estado = False
