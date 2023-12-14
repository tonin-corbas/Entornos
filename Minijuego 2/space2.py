import pygame
import elementos2
import random
#inicialicamos el juego
pygame.init()

#creamos la pantalla
tamanio = (800, 600)
pantalla = pygame.display.set_mode(tamanio)

#creamos un reloj
reloj = pygame.time.Clock()
FPS = 60

#booleano de control
running = True
posicion = (250,250)
nave = elementos2.Nave(posicion)

#crear un grupo de sprites
grupo_sprites = pygame.sprite.Group(nave)
grupo_sprites.add(elementos2.Nave((400,200)))
grupo_sprites.add(elementos2.Nave((500,100)))
grupo_sprites.add(elementos2.Nave((100,300)))


enemigo = elementos2.Enemigo((50,50))
grupo_sprites.add(elementos2.Enemigo((70, 70)))

#crear u na variable que almacene la última creacion de enemigo
ultimo_enemigo_creado = 0

#bucle principal
while running:
    #Limitamos el bucle al framrate definido
    reloj.tick(FPS)
    #gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #creacion de enemigos
    momento_actual = pygame.time.get_ticks()
   # if(momento_actual > ultimo_enemigo_creado + 180):
    #    cordX = random.randint(0, pantalla.get_width())
     #   cordY = 0
      #  grupo_sprites.add(elementos2.Enemigo((cordX, cordY)))
       # ultimo_enemigo_creado = momento_actual

    #capturamos las teclas
    teclas = pygame.key.get_pressed()

    #pintaremos:
    pantalla.fill((255,255,255))
    grupo_sprites.update(teclas)
    grupo_sprites.draw(pantalla)

    #redibujar la pantala
    pygame.display.flip()
#finalizamos el juego
pygame.quit()
