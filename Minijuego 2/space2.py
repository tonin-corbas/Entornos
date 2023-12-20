import pygame
import elementos2
import random
#inicialicamos el juego
pygame.init()

#creamos la pantalla
tamanio = (1000, 800)
pantalla = pygame.display.set_mode(tamanio)

#creamos un reloj
reloj = pygame.time.Clock()
FPS = 100

#booleano de control
running = True
posicion = (650,700)
nave = elementos2.Nave(posicion)
fondo = elementos2.Fondo()
#crear un grupo de sprites
#grupo_sprites = pygame.sprite.Group(fondo)
#grupo_sprites.add(nave)

#grupo_sprites.add(elementos2.Nave((400,200)))
#grupo_sprites.add(elementos2.Nave((500,100)))
#grupo_sprites.add(elementos2.Nave((100,300)))

grupo_sprites_todos = pygame.sprite.Group()
grupo_sprites_enemigos = pygame.sprite.Group()
grupo_sprites_bala = pygame.sprite.Group()

grupo_sprites_todos.add(fondo)
grupo_sprites_todos.add(nave)
#enemigo = elementos2.Enemigo((50,50))
#grupo_sprites.add(elementos2.Enemigo((70, 70)))

#crear u na variable que almacene la última creacion de enemigo
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 1500

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
    if(momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
        cordX = random.randint(0, pantalla.get_width())
        cordY = 0
        enemigo = elementos2.Enemigo((cordX, cordY))
        grupo_sprites_todos.add(enemigo)
        grupo_sprites_enemigos.add(enemigo)
        ultimo_enemigo_creado = momento_actual

    #capturamos las teclas
    teclas = pygame.key.get_pressed()
    #if teclas[pygame.K_SPACE]:
     #   nave.disparar(grupo_sprites_todos)

    #pintaremos:
    #pantalla.fill((255,255,255))
    grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_bala)
    grupo_sprites_todos.draw(pantalla)

    #redibujar la pantala
    pygame.display.flip()
#finalizamos el juego
pygame.quit()
