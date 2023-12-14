import pygame

class Nave (pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion) -> None:
        super().__init__()
        #cargamos la imagen
        self.imagenes = [pygame.image.load("avion4.png"), pygame.image.load("avion5.png")]
        self.indice_imagen = 0
        self.image = self.imagenes[self.indice_imagen]
        self.contador_imagen = 0
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion


    #update
    def update(self, *args: any, **kwargs: any) -> None:
        teclas = args[0]
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
            self.rect.x = max(0, self.rect.x)
        elif teclas[pygame.K_RIGHT]:
            self.rect.x += 2
            self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        #gestionamos
        self.contador_imagen = (self.contador_imagen + 1) % 40
        self.indice_imagen = self.contador_imagen // 20
        self.image = self.imagenes[self.indice_imagen]
#creador de enemigos
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        #cargamos la imagen
        imagen = pygame.image.load("avion4.png")
        self.image = pygame.transform.rotate(imagen, 180)
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: any, **kwargs: any):
        pantalla = pygame.display.get_surface()
        self.rect.y += 1
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
