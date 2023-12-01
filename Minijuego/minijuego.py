import pygame

pygame.init()
pantalla = pygame.display.set_mode((1000, 800))
imagen_avion = pygame.image.load("avion4.png")
avion = pygame.transform.scale(imagen_avion, (145, 170))
posIzda = 30
postop = 30
salir = False

while not salir:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            salir = True
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        posIzda -= 1
    elif teclas[pygame.K_RIGHT]:
        posIzda += 1
    elif teclas[pygame.K_UP]:
        postop -= 1
    elif teclas[pygame.K_DOWN]:
        postop += 1

    pantalla.fill((0, 80, 170))
    pantalla.blit(avion, (posIzda, postop))

    pygame.display.flip()

pygame.quit()
