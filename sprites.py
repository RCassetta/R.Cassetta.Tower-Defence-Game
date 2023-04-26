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