import pygame
import eljuego
import random
import pygame_menu

pygame.init()

# Creamos un reloj para los FPS
reloj = pygame.time.Clock()
FPS = 18

# Creamos la pantalla
pantalla = pygame.display.set_mode((1000, 800))
font = pygame.font.Font(None, 30)
fondo = eljuego.Fondo()
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 750

def set_difficulty(value, difficulty):
    # Do the job here !
    global frecuencia_creacion_enemigo
    frecuencia_creacion_enemigo = difficulty
    pass

def start_the_game():
    # Do the job here !
    running = [True]
    global ultimo_enemigo_creado
    global frecuencia_creacion_enemigo
    global FPS
    global reloj
    posicion = (500, 600)
    nave = eljuego.Nave(posicion)
    fondo = eljuego.Fondo()
    # crear un grupo de sprites
    # grupo_sprites = pygame.sprite.Group(fondo)
    # grupo_sprites.add(nave)

    # grupo_sprites.add(elementos2.Nave((400,200)))
    # grupo_sprites.add(elementos2.Nave((500,100)))
    # grupo_sprites.add(elementos2.Nave((100,300)))

    grupo_sprites_todos = pygame.sprite.Group()
    grupo_sprites_enemigos = pygame.sprite.Group()
    grupo_sprites_bala = pygame.sprite.Group()

     # grupo_sprites_todos.add(elementos2.Fondo, (0, - ))
    grupo_sprites_todos.add(fondo)
    grupo_sprites_todos.add(nave)

    pausado = False

    # capturamos las teclas

    # bucle principal
    while running[0]:
        # Limitamos el bucle al framrate definido
        reloj.tick(FPS)
        # gestionar la salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = [False]

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
            running[0] = False

        if teclas[pygame.K_SPACE]:
            pausado = not pausado


        if not pausado:
            # creacion de enemigos
            momento_actual = pygame.time.get_ticks()
            if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
                cordX = random.randint(0, pantalla.get_width())
                cordY = 0
                enemigo = eljuego.Enemigo((cordX, cordY))
                grupo_sprites_todos.add(enemigo)
                grupo_sprites_enemigos.add(enemigo)
                ultimo_enemigo_creado = momento_actual

            grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_bala, grupo_sprites_enemigos,
                                           running)

        # capturamos las teclas

        # pintaremos:
        # pantalla.fill((255,255,255))
        # grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_bala, grupo_sprites_enemigos, running)
        grupo_sprites_todos.draw(pantalla)

        if pausado:
            texto = font.render("PAUSA", True, "White")
            pantalla.blit(texto, (pantalla.get_width() / 2, pantalla.get_height() / 2))

        # redibujar la pantala
        pygame.display.flip()
    pass

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='')
menu.add.selector('Difficulty :', [('Hard', 200), ('Easy', 2000)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(pantalla)
pygame.quit()
