import pygame as pg
from settings import *
from sprites import *
import os


### ASSETS ###
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "assets")

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tower Defence Game")
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True
        background = pg.image.load("C:\\Users\\R.Cassetta24\\OneDrive - Bellarmine College Preparatory\\Desktop\\IntroCompSci\\Tower Defence Game VSCode\\assets\\background.png").convert()
        self.background = pg.transform.scale(background, (WIDTH, HEIGHT))

    def new(self):
        self.enemies = pg.sprite.Group()
        enemy = enemies(20, 20, RED)
        self.enemies.add(enemy)
        enemy.rect = enemy.image.get_rect(center=(0, HEIGHT/2))
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def run(self):
        while self.running:
            self.events()
            self.screen.blit(self.background, (0, 0))
            self.enemies.draw(self.screen)
            self.enemies.update()
            pg.display.flip()
            self.clock.tick(FPS)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.enemies.draw(self.screen)
        pg.display.flip()
        
        


game = Game()
game.new()
game.run()