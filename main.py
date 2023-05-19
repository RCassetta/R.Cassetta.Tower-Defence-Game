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
Add towers // DONE
Make towers attack Enemy // DONE
Add music // DONE
Make a menu // NA
'''
### SOURCES ###
# https://www.inspiredpython.com/course/create-tower-defense-game/make-your-own-tower-defense-game-with-pygame
# https://www.pygame.org/tags/towerdefense
# https://www.youtube.com/watch?v=iLHAKXQBOoA
# https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/projectiles

### Instructipns/ HOW TO PLAY ###
# To start first wave -> press p once
# To start every wave after 1st -> press p twice
# To pause enemy movement -> press p once and again to resume
# New towers cost 50$ and you earn $ by shooting the enemies
# In order to place a new tower, you must put the mouse in the position where you want the tower and click space bar
# MR. Cozort, if you play this, at least once let yourself die to the enemies for a surprise!
### CONTROLS ###
# p = pause/resume/start
# space = buy new tower

### ASSETS ###
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "assets")

### AUDIO ###
pg.mixer.init()
pg.mixer.music.load(path.join(img_folder, "theme_music.mp3"))
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.5)
death_sound = pg.mixer.Sound(path.join(img_folder, "death_sound.mp3"))

### GAME ###
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
        self.tower_group = pg.sprite.Group()
        self.Enemy = pg.sprite.Group()
        self.projectile_group = pg.sprite.Group()

### DEATH SCREEN ###
    def show_death_screen(self):
        self.screen.blit(self.death_screen, (0, 0))
        pg.mixer_music.stop()
        death_sound.play()
        pg.display.flip()

### ROUNDS ###
    def new(self):
        tower = Tower(200, 300, self.projectile_group)
        self.tower_group.add(tower)
        enemy_positions = []

### ROUND 1 ###
        if self.round == 1:
            for i in range(1, 11):
                if i > 5:
                    e = Enemy(self, 20, 20, BLUE, 2)
                else:
                    e = Enemy(self, 20, 20, RED, 1)
                x = -40 * i
                y = HEIGHT / 2
                enemy_positions.append((x, y))
                e.rect = e.image.get_rect(center=enemy_positions[i-1])
                self.Enemy.add(e)

### ROUND 2 ###
        if self.round == 2:
            for i in range(1, 31):
                if i > 15:
                    e = Enemy(self, 20, 20, BLUE, 2)
                else:
                    e = Enemy(self, 20, 20, RED, 1)
                x = -40 * i
                y = HEIGHT / 2
                enemy_positions.append((x, y))
                e.rect = e.image.get_rect(center=enemy_positions[i-1])
                self.Enemy.add(e)

### ROUND 3 ###
        if self.round == 3:
            for i in range(1, 41):
                if i > 30:
                    e = Enemy(self, 20, 20, BLUE, 2)
                else:
                    e = Enemy(self, 20, 20, RED, 1)
                x = -40 * i
                y = HEIGHT / 2
                enemy_positions.append((x, y))
                e.rect = e.image.get_rect(center=enemy_positions[i-1])
                self.Enemy.add(e)

### ROUND 4 ###
        if self.round == 4:
            for i in range(1, 71):
                if i > 50:
                    e = Enemy(self, 20, 20, BLUE, 2)
                else:
                    e = Enemy(self, 20, 20, RED, 1)
                x = -40 * i
                y = HEIGHT / 2
                enemy_positions.append((x, y))
                e.rect = e.image.get_rect(center=enemy_positions[i-1])
                self.Enemy.add(e)
                
### ROUND 5 ###
        if self.round == 5:
            for i in range(1, 101):
                if i > 70:
                    e = Enemy(self, 20, 20, BLUE, 2)
                else:
                    e = Enemy(self, 20, 20, RED, 1)
                x = -40 * i
                y = HEIGHT / 2
                enemy_positions.append((x, y))
                e.rect = e.image.get_rect(center=enemy_positions[i-1])
                self.Enemy.add(e)

### CONSTANTS/HEALTH UPDATE ###
    def run(self):
        while self.running:
            self.events()
            self.screen.blit(self.background, (0, 0))
            self.draw_player_info()
            self.Enemy.draw(self.screen)
            self.Enemy.update()
            self.clock.tick(FPS)
            self.projectile_group.update()
            self.tower_group.update(self.Enemy, self.projectile_group)
            self.projectile_group.draw(self.screen)
            self.tower_group.draw(self.screen)
            if len(self.Enemy) == 0:
                self.round += 1
                self.new()
            if self.player_health <= 0:
                self.game_over = True
            if self.game_over:
                self.show_death_screen()
            pg.display.flip()

### CONTROLS ###
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    self.path_enabled = not self.path_enabled
                    for enemy in self.Enemy:
                        enemy.path_enabled = self.path_enabled
                if event.key == pg.K_SPACE:
                    if self.player_money >=50:
                        mouse_pos = pg.mouse.get_pos()
                        self.spawn_tower(*mouse_pos)
                        self.player_money -= 50

### UPDATES ###
    def update(self):
        self.Enemy.update()
        
### DRAW UPDATES ###
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.Enemy.draw(self.screen)
        self.tower_group.draw(self.screen)
        pg.display.flip()

### HEALTH AND MONEY ###
    def draw_player_info(self):
        health_text = f"Health: {self.player_health}"
        money_text = f"Money: {self.player_money}"
        info_font = pg.font.Font(None, 30)
        health_surface = info_font.render(health_text, True, WHITE)
        money_surface = info_font.render(money_text, True, WHITE)

        self.screen.blit(health_surface, (20, 20))
        self.screen.blit(money_surface, (20, 60))

### SPAWNS TOWER WITH SPACE BAR/ HALF IN EVENTS ###   
    def spawn_tower(self, x, y):
        tower = Tower(x, y, self.projectile_group, )
        self.tower_group.add(tower)

### GAME CALLING ###
game = Game()
game.new()
game.run()