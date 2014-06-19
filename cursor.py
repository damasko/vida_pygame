import pygame


class Cursor(object):

    def __init__(self):

        self.rect = pygame.rect.Rect(0, 0, 6, 6)
        self.puntero = pygame.rect.Rect(0, 0, 1, 1)
        pygame.mouse.set_visible(False)

    def update(self):

        self.rect.x, self.rect.y = pygame.mouse.get_pos()
        self.puntero.x, self.puntero.y = self.rect.centerx, self.rect.centery

    def changeState(self, matriz):

        for fila in matriz:
            for cell in fila:
                if pygame.mouse.get_pressed()[0]:
                    if self.puntero.colliderect(cell.rect):

                        cell.estado = True

                if pygame.mouse.get_pressed()[2]:

                    if self.puntero.colliderect(cell.rect):

                        cell.estado = False
