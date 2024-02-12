import pygame
import eljuego
import pygame_menu

pygame.init()

# Creamos un reloj para los FPS
reloj = pygame.time.Clock()
FPS = 18

# Creamos la pantalla
espacio = (1920,1080)
espacio_pequeno = (1920/2,1080/2)
screen = pygame.display.set_mode(espacio, pygame.FULLSCREEN)
# pantalla = pygame.display.set_mode((1000, 800))
font = pygame.font.Font(None, 30)
fondo = eljuego.Fondo()
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 750
velocidad_enemigo = 10
screen_actual = False

def set_difficulty(value, difficulty):
    global frecuencia_creacion_enemigo
    global velocidad_enemigo
    frecuencia_creacion_enemigo = difficulty

    if difficulty == 200:
        velocidad_enemigo = 15
    else:
        velocidad_enemigo = 10

def start_the_game():
    # Do the job here !
    running = [True]
    global ultimo_enemigo_creado
    global frecuencia_creacion_enemigo
    global FPS
    global reloj

    vida = 3
    puntuacion = 0

    parametros = eljuego.Parametros()

    posicion = (250, 350)
    posicionP = (screen.get_width() / 2.025, screen.get_height() * 1.5)
    # screen.get_width() / 2, screen.get_height() * 1.75
    nave = eljuego.Nave(posicion)
    fondo = eljuego.Fondo()
    planeta = eljuego.Planeta(posicionP)

    grupo_sprites_todos = pygame.sprite.Group()
    grupo_sprites_enemigos = pygame.sprite.Group()
    grupo_sprites_bala = pygame.sprite.Group()
    grupo_sprites_planeta = pygame.sprite.Group()

    grupo_sprites_todos.add(fondo)
    grupo_sprites_todos.add(planeta)
    grupo_sprites_todos.add(nave)
    grupo_sprites_planeta.add(planeta)


    pausado = False

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

        if teclas[pygame.K_p]:
            pausado = not pausado


        if not pausado:
            # creacion de enemigos
            numero_enemigos = 1
            enemigos_por_fila = 1
            enemigos_creados = 0
            enemigos_bajados = 0

            if not pausado:
                # creacion de enemigos
                momento_actual = pygame.time.get_ticks()
                if enemigos_creados < numero_enemigos and (
                        momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
                    for i in range(enemigos_por_fila):
                        cordX = i * (screen.get_width() / enemigos_por_fila)
                        cordY = 0
                        enemigo = eljuego.Enemigo((cordX, cordY))
                        grupo_sprites_enemigos.add(enemigo)
                        grupo_sprites_todos.add(enemigo)
                        enemigos_creados += 1
                    ultimo_enemigo_creado = momento_actual

                # Comprobar si todos los enemigos de una fila han bajado
                for enemigo in grupo_sprites_enemigos:
                    if enemigo.rect.y > screen.get_height() / 2:
                        enemigos_bajados += 1
                        grupo_sprites_enemigos.remove(enemigo)
                        grupo_sprites_todos.remove(enemigo)

                # Si todos los enemigos de una fila han bajado, resetea los contadores
                if enemigos_bajados == enemigos_por_fila:
                    enemigos_creados = 0
                    enemigos_bajados = 0

            grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_bala, grupo_sprites_enemigos,
                                           running, grupo_sprites_planeta, parametros)
        grupo_sprites_todos.draw(screen)

        vidas = font.render(f"Vidas: {parametros.getVidas()}", True, "White")
        screen.blit(vidas, (10, 20))
        puntos = font.render(f"Puntos: {parametros.getPuntuacion()} ", True, "White")
        screen.blit(puntos, (10, 40))


        if pausado:
            texto = font.render("PAUSA", True, "White")
            screen.blit(texto, (screen.get_width() / 2, screen.get_height() / 2))
        # redibujar la pantala
        pygame.display.flip()
    pass

menu = pygame_menu.Menu('Buenas', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('ID :', default='')
menu.add.selector('Dificultad :', [('Fácil', 2000), ('Difícil', 200)], onchange=set_difficulty)
menu.add.button('Jogar', start_the_game)
menu.add.button('Finalizar', pygame_menu.events.EXIT)

menu.mainloop(screen)
pygame.quit()
