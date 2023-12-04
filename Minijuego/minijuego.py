import pygame
from elementos import Nave

pygame.init()
pantalla = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
FPS = 60
imagen_avion = pygame.image.load("avion4.png")
avion = pygame.transform.scale(imagen_avion, (145, 170))
#posIzda = 30
#postop = 30
salir = False

nave = Nave()

while not salir:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
       nave.moverIzquierda()
    elif teclas[pygame.K_RIGHT]:
        nave.moverDerecha()
    #elif teclas[pygame.K_UP]:
     #   postop -= 1
    #elif teclas[pygame.K_DOWN]:
    #    postop += 1

    pantalla.fill((0, 80, 170))
    #pantalla.blit(avion, (posIzda, postop))
    nave.dibujar()
    pygame.display.flip()

pygame.quit()
