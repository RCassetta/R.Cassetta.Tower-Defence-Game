import pygame as pg
from settings import *
from sprites import *
import os
from os import path
from time import time

'''
GOALS:
Create enemy path // DONE
Add enemy // DONE
Add multiple Enemy // WIP
Add enemy types // NA
Add rounds // WIP
Add player health // DONE
Add towers // NA
Make towers attack Enemy // NA
Add music // DONE
Make a menu // NA
'''
### Instructipns ###
# Place towers before the round starts
# THe round will only start if you click SPACE, followed with P
# WHen the round ends, you must click P twice in order to move to the next round

### CONTROLS ###
# Space = skip to next round
# P = play round


### ASSETS ###
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "assets")

pg.mixer.init()
pg.mixer.music.load("theme_music.mp3")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(.5)

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tower Defense Game")
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True
        background = pg.image.load(path.join(img_folder, "background.png")).convert()
        self.background = pg.transform.scale(background, (WIDTH, HEIGHT))
        self.path_enabled = False
        self.round = 0
        self.player_health = 100

    def new(self):
        self.Enemy = pg.sprite.Group()
        enemy_positions = []
        if self.round == 1:
            for i in range(1,10):
                if i > 5:
                    e = Enemy(self, 20, 20, BLUE)
                else:
                    e = Enemy(self, 20, 20, RED)
                x = -40 * i
                y = HEIGHT / 2
                enemy_positions.append((x,y))
                e.rect = e.image.get_rect(center=enemy_positions[i-1])
                self.Enemy.add(e)

        if self.round == 2:
            for i in range(1,30):
                if i > 15:
                    e = Enemy(self, 20, 20, BLUE)
                else:
                    e = Enemy(self, 20, 20, RED)
                x = -40 * i
                y = HEIGHT / 2
                enemy_positions.append((x,y))
                e.rect = e.image.get_rect(center=enemy_positions[i-1])
                self.Enemy.add(e)
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                #   self.round += 1
                #   self.new()
                  self.path_enabled = not self.path_enabled
                  for enemy in self.Enemy:
                      enemy.path_enabled = self.path_enabled 
                if event.key == pg.K_SPACE:
                    self.round +=1
                    self.new()
                    print(self.round)

    def run(self):
        while self.running:
            self.events()
            self.screen.blit(self.background, (0, 0))
            self.Enemy.draw(self.screen)
            self.Enemy.update()
            pg.display.flip()
            self.clock.tick(FPS)

    def update(self):
        self.Enemy.update()
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.Enemy.draw(self.screen)
        pg.display.flip()

        


game = Game()
game.new()
game.run()