import pygame

class Nave:
    def __init__(self) -> None:
        self.x = 500
        self.y = 200
        self.imagen = [pygame.image.load("avion4.png"), pygame.image.load("avion5.png")]
        self.contador = 0

    def moverDerecha(self):
        self.x += 5.5
        pantalla = pygame.display.get_surface()
        tamanio_pantalla = pantalla.get_width()
        limite = tamanio_pantalla - self.imagen[0].get_width()
        self.x = min(self.x, limite)

    def moverIzquierda(self):
        self.x -= 5.5
        pantalla = pygame.display.get_surface()
        limite = 0
        self.x = max(self.x, limite)

    def dibujar(self):
        self.contador = (self.contador + 1) % 40
        pantalla = pygame.display.get_surface()
        seleccionada = self.contador // 20
        pantalla.blit(self.imagen[seleccionada], (self.x, self.y))
