import pygame
import sys

# Inicialitzar pygame
pygame.init()

# Constants
AMPLADA, ALÇADA = 800, 600
FPS = 60
VEL_BOLA = 5
VEL_RAQUETA = 10
BLOC_FILA, BLOC_COL = 5, 10

# Colors
BLANC = (255, 255, 255)
NEGRO = (0, 0, 0)
RED = (255,0,0)

# Pantalla
pantalla = pygame.display.set_mode((AMPLADA, ALÇADA))
pygame.display.set_caption("Arkanoid Simple")

# Raqueta
raqueta = pygame.Rect(AMPLADA//2 - 50, ALÇADA - 30, 100, 10)

# Bola
bola = pygame.Rect(AMPLADA//2 - 10, ALÇADA//2, 20, 20)
dir_x, dir_y = VEL_BOLA, -VEL_BOLA
joc_actiu = False

# Blocs
blocs = []
for fila in range(BLOC_FILA):
    for col in range(BLOC_COL):
        bloc = pygame.Rect(60*col + 10, 30*fila + 50, 50, 20)
        blocs.append(bloc)

# Rellotge
rellotge = pygame.time.Clock()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                joc_actiu = True

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and raqueta.left > 0:
        raqueta.x -= VEL_RAQUETA
    if teclas[pygame.K_RIGHT] and raqueta.right < AMPLADA:
        raqueta.x += VEL_RAQUETA

    if joc_actiu:
        # Mou la bola
        bola.x += dir_x
        bola.y += dir_y

        # Col·lisions amb parets
        if bola.left <= 0 or bola.right >= AMPLADA:
            dir_x *= -1
        if bola.top <= 0:
            dir_y *= -1
        if bola.bottom >= ALÇADA:
            joc_actiu = False
            bola.x, bola.y = AMPLADA//2 - 10, ALÇADA//2

        # Col·lisió amb raqueta
        if bola.colliderect(raqueta):
            dir_y *= -1

        # Col·lisions amb blocs
        for bloc in blocs[:]:
            if bola.colliderect(bloc):
                blocs.remove(bloc)
                dir_y *= -1
                break

    # Dibuixar
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, BLANC, raqueta)
    pygame.draw.ellipse(pantalla, RED, bola)
    for bloc in blocs:
        pygame.draw.rect(pantalla, BLANC, bloc)

    pygame.display.flip()
    rellotge.tick(FPS)
