import math

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

class Fondo:
    def __init__(self) -> None:
        # localizar la pantalla
        pantalla = pygame.display.get_surface()
        # cargamos la imagen
        imagen = pygame.image.load("fondo.jpg")
        self.fondo = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height()))
        #scroll
        self.scroll = 0
        #cuantas piezas de fondo se necesitan
        self.piezas = math.ceil(pantalla.get_height() / self.fondo.get_height()) + 1

    def dibujar(self):
        #aumentar el scroll
        self.scroll += 7
        #localizar la pantalla
        pantalla = pygame.display.get_surface()
        #rescatar scroll
        if self.scroll > self.fondo.get_height():
            self.scroll = 0
        #dibujamos el fondo
        pantalla.blit(self.fondo, (0,self.scroll))
        for i in range(0, self.piezas):
            pantalla.blit(self.fondo, (0, - self.fondo.get_height() + i * self.fondo.get_height() + self.scroll))
