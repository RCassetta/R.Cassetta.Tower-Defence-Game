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
Add multiple Enemy // DONE
Add enemy types // DONE
Add rounds // DONE
Add player health // DONE
Add money // DONE
Add towers // WIP
Make towers attack Enemy // NA
Add music // DONE
Make a menu // NA
'''
### Instructipns ###
# To start first wave -> press p once
# To start every wave after 1st -> press p twice
# To pause enemy movement -> press p once and again to resume

### CONTROLS ###
# p = pause/resume/start


### ASSETS ###
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "assets")

pg.mixer.init()
pg.mixer.music.load("theme_music.mp3")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.5)
death_sound = pg.mixer.Sound("death_sound.mp3")

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
        self.death_screen = pg.image.load(path.join(img_folder, "death_screen.png")).convert()
        self.death_screen = pg.transform.scale(self.death_screen, (WIDTH, HEIGHT))
        self.path_enabled = False
        self.round = 0
        self.player_health = 100
        self.player_money = 100
        self.game_over = False


    def show_death_screen(self):
        self.screen.blit(self.death_screen, (0, 0))
        pg.mixer_music.stop()
        death_sound.play()
        pg.display.flip()

    def new(self):
        self.Enemy = pg.sprite.Group()
        enemy_positions = []
        if self.round == 1:
            for i in range(1,11):
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
            for i in range(1,31):
                if i > 15:
                    e = Enemy(self, 20, 20, BLUE)
                else:
                    e = Enemy(self, 20, 20, RED)
                x = -40 * i
                y = HEIGHT / 2
                enemy_positions.append((x,y))
                e.rect = e.image.get_rect(center=enemy_positions[i-1])
                self.Enemy.add(e)

        if self.round == 3:
            for i in range(1,61):
                if i > 30:
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
                    self.player_money -= 1
                    self.new()
                    print(self.player_money)

    def run(self):
        while self.running:
            self.events()
            self.screen.blit(self.background, (0, 0))
            self.draw_player_info()
            self.Enemy.draw(self.screen)
            self.Enemy.update()
            self.clock.tick(FPS)
            if len(self.Enemy) == 0:
                self.round += 1
                self.new()
            if self.player_health <= 0:
                self.game_over = True
            if self.game_over:
                self.show_death_screen()
            pg.display.flip()

    def update(self):
        self.Enemy.update()
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.Enemy.draw(self.screen)
        pg.display.flip()
    def draw_player_info(self):
        health_text = f"Health: {self.player_health}"
        money_text = f"Money: {self.player_money}"
        
        info_font = pg.font.Font(None, 30)  # Adjust the font size as needed
        
        health_surface = info_font.render(health_text, True, WHITE)
        money_surface = info_font.render(money_text, True, WHITE)
        
        self.screen.blit(health_surface, (20, 20))  # Adjust the position as needed
        self.screen.blit(money_surface, (20, 60))  # Adjust the position as needed
        


game = Game()
game.new()
game.run()