import pygame as pg
from settings import *
from sprites import *
import os

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
        background = pg.image.load("C:\\Users\\R.Cassetta24\\OneDrive - Bellarmine College Preparatory\\Desktop\\IntroCompSci\\Tower Defence Game VSCode\\assets\\background.png").convert()
        self.background = pg.transform.scale(background, (WIDTH, HEIGHT))
        self.path_enabled = False

    def new(self):
        self.enemies = pg.sprite.Group()
        for enemy in ENEMY_LIST:
            new_enemy = enemies(*enemy)
            self.enemies.add(new_enemy)
            new_enemy.rect = new_enemy.image.get_rect(center=(0, HEIGHT/2))
            enemy_colors = ([RED] * ENEMY_COUNT)
            enemy_positions = []
        for i in range(ENEMY_COUNT):
            x = -40 * i
            y = HEIGHT / 2
            enemy_positions.append((x, y))
        for i in range(len(enemy_colors)):
            enemy = enemies(20, 20, enemy_colors[i])
            self.enemies.add(enemy)
            enemy.rect = enemy.image.get_rect(center=enemy_positions[i])
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

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.enemies.draw(self.screen)
        pg.display.flip()

        


game = Game()
game.new()
game.run()