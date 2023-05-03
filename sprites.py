import pygame as pg
# from main import *
from settings import *
from pygame.sprite import Sprite
        
class enemies(Sprite):
    def __init__(self, width, height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self):
        # Seg 1
            if self.rect.y == 415 and self.rect.x <=330:
                self.rect.x += 5 
            # Seg 2
            if self.rect.x == 330 and self.rect.y <500:
                self.rect.y -=5
            # Seg 3
            if self.rect.y == 110:
                self.rect.x +=5
            # Seg 4
            if self.rect.x == 615 and self.rect.y <600:
                self.rect.y += 5
            # Seg 5
            if self.rect.y == 575 and self.rect.x <800:
                self.rect.x -= 5
            # Seg 6
            if self.rect.x == 205 and self.rect.y >500:
                self.rect.y +=5
            # Seg 7
            if self.rect.y == 725:
                self.rect.x +=5
            # Seg 8
            if self.rect.x == 1175 and self.rect.y >=400:
                self.rect.y -= 5
            # Seg 9
            if self.rect.y == 500 and self.rect.x > 700:
                self.rect.x -=5
            # seg 10
            if self.rect.x == 900 and self.rect.y <= 500:
                self.rect.y -= 5
            # seg 11
            if self.rect.y == 190 and self.rect.x >=900:
                self.rect.x +=5