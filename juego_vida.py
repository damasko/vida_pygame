import pygame
import random
from cursor import Cursor
from cell import Cell

# variables globales bla bla bla
green = (0, 250, 0)
red = (250, 0, 0)
black = (0, 0, 0)
grey = (55, 55, 55)


def rellenaRandom(lista):

    for i in range(1, len(lista) - 1):
        for j in range(1, len(lista[0]) - 1):

            #Le doy mas probabilidades a que este muerta que viva
            n = random.randint(0, 3)
            if (n == 0):
                lista[i][j].estado = True
            else:
                lista[i][j].estado = False

    return lista


def isAlive(lista_celulas):

    lista_estados = []
    for i in lista_celulas:
        linea = []
        for j in i:
            estado = j.estado
            linea.append(estado)
        lista_estados.append(linea)

    #print "estados " + str(len(lista_estados))
    #print "celulas " + str(len(lista_celulas))

    vecinos = 0
    for i in range(0, len(lista_estados) - 1):
        for j in range(0, len(lista_estados[i]) - 1):

            if i != 0 or j != 0:
                if (lista_estados[i - 1][j - 1]):
                    vecinos += 1

                if (lista_estados[i - 1][j]):
                    vecinos += 1

                if (lista_estados[i - 1][j + 1]):
                    vecinos += 1

                if (lista_estados[i][j + 1]):
                    vecinos += 1

                if (lista_estados[i + 1][j + 1]):
                    vecinos += 1

                if (lista_estados[i + 1][j]):
                    vecinos += 1

                if (lista_estados[i + 1][j - 1]):
                    vecinos += 1

                if (lista_estados[i][j - 1]):
                    vecinos += 1

                if (vecinos == 3):

                    lista_celulas[i][j].estado = True

                elif (vecinos == 2):

                    pass  # de momento con pass nos ahorramos reasignarlo

                else:

                    lista_celulas[i][j].estado = False

                vecinos = 0

            else:

                lista_celulas[i][j].estado = False

    return lista_celulas


def dibuja_mapa(lista_celulas, screen):

    for fila in lista_celulas:
        for celula in fila:
            if celula.estado:
                pygame.draw.rect(screen, green, celula.rect)
            else:
                pygame.draw.rect(screen, grey, celula.rect)


def clearArray(matriz):

    for fila in matriz:
        for cell in fila:
            cell.estado = False


def main():

    if (not pygame.init()):
        return -1

    x = 3
    y = 3

    #matrix = [[pygame.Rect(x,y,h,w) for i in range(50)] for j in range(50)]
    #Ordenar rectangulos en forma de cuadricula
    matrix = []
    for i in range(80):
        linea = []
        for j in range(110):
            celula = Cell(x, y)
            linea.append(celula)
            x += 9
        matrix.append(linea)
        x = 3
        y += 9

    cursor1 = Cursor()
    pygame.mouse.set_visible = False
    screen = pygame.display.set_mode((len(matrix[0]) * 9, y + 30))
    pygame.display.set_caption("Game of Life")
    salir = False
    pygame.font.init()
    fuente = pygame.font.SysFont("default", 24)
    numero = 0
    texto = fuente.render("Space: Continue/Stop    R (in pause): Random Board    1/2: + / - Speed    C (in pause): Clear Board"
                , True, (0, 255, 125))
    screen.blit(texto, (5, screen.get_height() - 25))
    velocidad = 25

    #reloj para los fps
    clock = pygame.time.Clock()
    #colores
    #white=(255,255,255)
    #Relleno la lista con valores aleatorios (ya no es necesario)
    #matrix = rellenaRandom(matrix)
    #cursor1=Cursor()
    pausa = True

    while not salir:

        generacion = fuente.render("  Generation: " + str(numero),
                    True, (0, 255, 125))
        clock.tick(int(2 * velocidad / 3))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausa = True
                if event.key == pygame.K_2:
                    if velocidad < 95:
                        velocidad += 5
                if event.key == pygame.K_1:
                    if velocidad > 10:
                        velocidad -= 5

        if pausa:
            while pausa:
                # codigo repetido, para evitarlo crear un eventhandler
                cursor1.update()
                clock.tick(velocidad)
                generacion = fuente.render("  Generation: " + str(numero),
                    True, (0, 255, 125))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pausa = False
                        salir = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:

                            pausa = False

                        if event.key == pygame.K_c:
                            clearArray(matrix)
                        if event.key == pygame.K_r:
                                rellenaRandom(matrix)
                        if event.key == pygame.K_2:
                            if velocidad < 95:
                                velocidad += 5
                        if event.key == pygame.K_1:
                            if velocidad > 10:
                                velocidad -= 5
                        if event.key == pygame.K_0:
                                numero = 0

                cursor1.update()
                cursor1.changeState(matrix)
                screen.fill(black)
                dibuja_mapa(matrix, screen)
                pygame.draw.rect(screen, (255, 0, 0), cursor1.rect)
                screen.blit(texto, (5, screen.get_height() - 25))
                screen.blit(generacion, (screen.get_width() - 250,
                            screen.get_height() - 25))
                pygame.display.update()

        cursor1.update()
        cursor1.changeState(matrix)

        screen.fill(black)
        screen.blit(texto, (5, screen.get_height() - 25))
        screen.blit(generacion, (screen.get_width() - 250, screen.get_height() - 25))
        matrix = isAlive(matrix)
        #Dibujar rectangulos en funcion de la lista comp
        dibuja_mapa(matrix, screen)
        numero += 1
        pygame.draw.rect(screen, (255, 0, 0), cursor1.rect)
        pygame.display.update()

    pygame.quit()
    return 0

main()

