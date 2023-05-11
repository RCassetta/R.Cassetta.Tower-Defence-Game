import pygame as pg
from settings import *
from sprites import *
import os
from os import path

'''
GOALS:
Create enemy path // DONE
Add enemy // DONE
Add multiple enemies // WIP
Add enemy types // NA
Add rounds // NA
Add player health // DONE
Add towers // NA
Make towers attack enemies // NA
'''

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
        background = pg.image.load(path.join(img_folder, "background.png")).convert()
        self.background = pg.transform.scale(background, (WIDTH, HEIGHT))
        self.path_enabled = False

    def new(self):
        self.enemies = pg.sprite.Group()
        self.player_health = 100
        enemy_positions = []
        for i in range(1,10):
            if i > 5:
                e = Enemy(self, 20, 20, BLUE)
            else:
                e = Enemy(self, 20, 20, RED)
            x = -40 * i
            y = HEIGHT / 2
            enemy_positions.append((x,y))
            e.rect = e.image.get_rect(center=enemy_positions[i-1])
            self.enemies.add(e)
        

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pg.KEYDOWN:
              if event.key == pg.K_p:
                  self.path_enabled = not self.path_enabled
                  for enemy in self.enemies:
                      enemy.path_enabled = self.path_enabled  

    def run(self):
        while self.running:
            self.events()
            self.screen.blit(self.background, (0, 0))
            self.enemies.draw(self.screen)
            self.enemies.update()
            pg.display.flip()
            self.clock.tick(FPS)
    def update(self):
        self.enemies.update()
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.enemies.draw(self.screen)
        pg.display.flip()

        


game = Game()
game.new()
game.run()