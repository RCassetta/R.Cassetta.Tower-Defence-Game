import pygame as pg
# from main import *
from settings import *
from pygame.sprite import Sprite
        
class eneies(Sprite):
    def __init__(self, width, height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        