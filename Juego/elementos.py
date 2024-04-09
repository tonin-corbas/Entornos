import pygame
import random


class Nave(pygame.sprite.Sprite):
    # Hacemos el contructor
    def __init__(self, posicion):
        super().__init__()
        self.naves = [pygame.image.load("navejuego.png"), pygame.image.load("navejuego3.png")]
        self.naves2 = [pygame.transform.scale(self.naves[0], (106.5 / 1.25, 110.5 / 1.25)),
                       pygame.transform.scale(self.naves[1], (106.5 / 1.25, 80 / 1.25))]
        self.indice_naves = 0
        self.contador_nave = 0
        # Rectangulo a partir de la nave
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.ultimo_tiro = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.cooldown = 1000  # Tiempo de cooldown en milisegundos (3 segundos)
        self.ultimo_disparo = pygame.time.get_ticks()  # Inicializa el tiempo del último disparo


    def disparar(self, grupo_sprites_todos, grupo_sprites_bala):
        actualidad = pygame.time.get_ticks()
        if actualidad - self.ultimo_disparo > self.cooldown:  # Verifica el cooldown
            bala = Bala((self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_width() / 5))
            grupo_sprites_bala.add(bala)
            grupo_sprites_todos.add(bala)
            self.ultimo_disparo = actualidad  # Actualiza el tiempo del último disparo
    def update(self, *args, **kwargs) -> None:
        # miramos teclas
        teclas = args[0]
        # miramos la pantallla
        pantalla = pygame.display.get_surface()
        grupo_sprites_todos = args[1]
        # miarmos balas
        grupo_sprites_bala = args[2]
        # Capturar grupo sprites enemigos 3
        grupo_sprites_enemigos = args[3]
        # miramos el run
        running = args[4]
        # grupo sprites planeta
        grupo_sprites_planeta = args[5]
        # Grupo bala enemigo
        grupo_sprites_bala_enemigo = args[7]
        # grupo enemigo fuerte
        grupo_sprites_enemigos_fuertes = args[8]


        # planeta colision
        planeta_colision = pygame.sprite.spritecollideany(self, grupo_sprites_planeta, pygame.sprite.collide_mask)

        # Preparamos las teclas
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and not planeta_colision:
            self.rect.x -= 20
            self.rect.x = max(0, self.rect.x)
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and not planeta_colision:
            self.rect.x += 20
            self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.rect.y -= 20
            self.rect.y = max(0, self.rect.y)
        if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and not planeta_colision:
            self.rect.y += 20
            self.rect.y = min(pantalla.get_width() - self.image.get_width(), self.rect.y)
        if teclas[pygame.K_SPACE]:
            self.disparar(grupo_sprites_todos, grupo_sprites_bala)

        # Hacemos la transicion de sprites
        self.contador_nave = (self.contador_nave + 5) % 40
        self.indice_naves = self.contador_nave // 30
        self.image = self.naves2[self.indice_naves]
        # detectar colisiones
        enemigo_colision = pygame.sprite.spritecollideany(self, grupo_sprites_enemigos, pygame.sprite.collide_mask)
        parametros = args[6]
        if enemigo_colision:
            enemigo_colision.kill()
            parametros.restarVida()
            parametros.restarPuntuacion()

        if parametros.getVidas() < 0:
            running[0] = False

        bala_enemigo_colision = pygame.sprite.spritecollideany(self, grupo_sprites_bala_enemigo,
                                                               pygame.sprite.collide_mask)
        parametros = args[6]
        if bala_enemigo_colision:
            bala_enemigo_colision.kill()
            parametros.restarVida()

        bala_enemigo_colision = pygame.sprite.spritecollideany(self, grupo_sprites_bala_enemigo,
                                                               pygame.sprite.collide_mask)
        parametros = args[6]
        if bala_enemigo_colision:
            bala_enemigo_colision.kill()
            parametros.restarVida()


class Planeta(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        # Cargamos imagen imagen del planeta
        planeta = pygame.image.load("planet.png")
        self.image = pygame.transform.scale(planeta, (2200, 1250))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

def update(self, *args: any, **kwargs: any):
        grupo_sprites_enemigos = args[3]
        running = args[4]
        enemigo_colision = pygame.sprite.spritecollideany(self, grupo_sprites_enemigos, pygame.sprite.collide_mask)
        parametros = args[6]
        if enemigo_colision:
            enemigo_colision.kill()
            parametros.restarVida()
            parametros.restarPuntuacion()

        if parametros.getVidas() < 0:
            running[0] = False


class Parametros:
    def __init__(self):
        self.vidas = 3
        self.puntuacion = 0

    def restarVida(self):
        self.vidas -= 1

    def sumarPuntuacion(self):
        self.puntuacion += 10

    def restarPuntuacion(self):
        self.puntuacion -= 20

    def getPuntuacion(self):
        return self.puntuacion

    def getVidas(self):
        return self.vidas

class Enemigo(pygame.sprite.Sprite):
    # Hacemos el contructor
    def __init__(self, posicion, velocidad_enemigo, grupo_sprites_planeta):
        super().__init__()
        self.image = pygame.image.load("enemigo1.png")
        self.mask = pygame.mask.from_surface(self.image)
        # Ajustamos el tamaño
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() / 1.5), int(self.image.get_height() / 1.5)))
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.velocidad_enemigo = velocidad_enemigo
        self.grupo_sprites_planeta = grupo_sprites_planeta

    def update(self, *args: any, **kwargs: any):
        self.rect.y += self.velocidad_enemigo

        if self.rect.y > pygame.display.get_surface().get_height():
            self.kill()

        colision_planeta = pygame.sprite.spritecollideany(self, self.grupo_sprites_planeta, pygame.sprite.collide_mask)
        if colision_planeta:
            self.kill()

class EnemigoFuerte(pygame.sprite.Sprite):
    # Hacemos el contructor
    def __init__(self, posicion, velocidad_enemigo, grupo_sprites_planeta):
        super().__init__()
        self.image = pygame.image.load("enemigo2.png")
        self.mask = pygame.mask.from_surface(self.image)
        # Ajustamos el tamaño
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() / 1.5), int(self.image.get_height() / 1.5)))
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.velocidad_enemigo = velocidad_enemigo
        self.grupo_sprites_planeta = grupo_sprites_planeta

    def update(self, *args: any, **kwargs: any):
        self.rect.y += self.velocidad_enemigo

        if self.rect.y > pygame.display.get_surface().get_height():
            self.kill()

        colision_planeta = pygame.sprite.spritecollideany(self, self.grupo_sprites_planeta, pygame.sprite.collide_mask)
        if colision_planeta:
            self.kill()


class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.image = pygame.image.load("bala.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any):
        self.rect.y -= 40
        if self.rect.y < 0:
            self.kill()