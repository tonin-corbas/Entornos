import pygame

class Nave (pygame.sprite.Sprite):
    # Hacemos el contructor
    def __init__(self, posicion):
        super().__init__()
        self.naves = [pygame.image.load("navejuego.png"), pygame.image.load("navejuego3.png")]
        self.naves2 = [pygame.transform.scale(self.naves[0], (70, 100)),  pygame.transform.scale(self.naves[1], (70, 100))]
        self.indice_naves = 0
        self.image = self.naves2[self.indice_naves]
        self.mask = pygame.mask.from_surface(self.image)
        self.contador_nave = 0
        # Rectangulo a partir de la nave
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.ultimo_tiro = 0

    def disparar(self,grupo_sprites_todos, grupo_sprites_bala):
        actualidad = pygame.time.get_ticks()
        if actualidad > self.ultimo_tiro + 200:
            bala = Bala((self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_width() / 2))
            grupo_sprites_bala.add(bala)
            grupo_sprites_todos.add(bala)
            self.ultimo_tiro = actualidad

    def  update(self, *args, **kwargs) -> None:
        teclas = args[0]
        # miramos la pantallla
        pantalla = pygame.display.get_surface()
        # miramos teclas
        grupo_sprites_todos = args[1]
        # miarmos balas
        grupo_sprites_bala = args[2]
        # Preparamos las teclas
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= 10
            self.rect.x = max(0, self.rect.x)
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += 10
            self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        if teclas[pygame.K_UP] or teclas[pygame.K_b]:
            self.disparar(grupo_sprites_todos, grupo_sprites_bala)
        # Hacemos la transicion de sprites
        self.contador_nave = (self.contador_nave + 5) % 40
        self.indice_naves = self.contador_nave // 30
        self.image = self.naves[self.indice_naves]
        # Capturar grupo sprites enemigos 3
        grupo_sprites_enemigos = args[3]


        running = args[4]
        # detectar colisiones
        enemigo_colision = pygame.sprite.spritecollideany(self, grupo_sprites_enemigos, pygame.sprite.collide_mask)
        if enemigo_colision:
            enemigo_colision.kill()
            running[0] = False

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        #cargamos la imagen
        imagen = pygame.image.load("avion4.png")
        imagen2 = pygame.transform.scale(imagen, (80, 140))
        self.image = pygame.transform.rotate(imagen2, 180)
        self.mask = pygame.mask.from_surface(self.image)
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: any, **kwargs: any):
        pantalla = pygame.display.get_surface()
        self.rect.y += 5
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        if (self.rect.y > pantalla.get_height()):
            self.kill()

        #capturar arg 2 bala
        grupo_sprites_bala = args[2]
        grupo_sprites_todos = args[1]
        bala_colision = pygame.sprite.spritecollideany(self, grupo_sprites_bala, pygame.sprite.collide_mask)
        if bala_colision:
            self.kill()
            bala_colision.kill()

class Fondo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        # cargamos la imagen
        imagen = pygame.image.load("fondo.jpg")
        #pantalla
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height()))
        # creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = (0, 0)

    #def update(self, *args: any, **kwargs: any) -> None:
      #self.rect.y +=1
      #capturamos pantalla
      #pantalla = pygame.display.get_surface()
      #if self.rect.y >= pantalla.get_height():
          #self.rect.y = - pantalla.get_height()

class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.y -=10
