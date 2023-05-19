import pygame as pg
# from main import *
from settings import *
from pygame.sprite import Sprite
import os
from os import path
import math

### ASSETS ###
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "assets")

### ENEMY CLASS ###
class Enemy(Sprite):
    def __init__(self, game, width, height, color, health):
        Sprite.__init__(self)
        self.game = game
        self.width = width
        self.height = height
        self.color = color
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.path_enabled = False
        self.health = health
        # DAMAGE TO PLAYER HEALTH
        if color == RED:
            self.health = 2
        elif color == BLUE:
            self.health = 1
        else:
            self.health = health

        self.image.fill(self.color)

### ENEMY PATH ### 
    def path(self):
        # print(self.rect.x)
        # print(self.rect.y)
        if self.path_enabled:
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

### UPDATES ###
    def update(self):
        # print(self.rect.x)
        if self.path_enabled:
            self.path()
        if self.rect.x >= WIDTH and self.game.player_health > 0:
            self.game.player_health -= self.health
            print(self.game.player_health)
            if self.game.player_health <= 0:
                print("Player Died")
                return True
            self.kill()
        return False
    
### TOWER CLASS ###
class Tower(Sprite):
    def __init__(self, x, y, projectile_group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(img_folder, "tower.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.range = 200
        self.damage = 10
        self.attack_cooldown = 1
        self.last_attack_time = pg.time.get_ticks()
        self.projectile_group = projectile_group

### TOWER UPDATES ###
    def update(self, enemies, projectile_group):
        now = pg.time.get_ticks()
        if now - self.last_attack_time >= self.attack_cooldown * 1000:
            target = self.find_target(enemies)
            if target:
                self.attack(target, projectile_group)
                self.last_attack_time = now

### TARGET FOR TOWERS ###
    def find_target(self, enemies):
        for enemy in enemies:
            if self.rect.centerx - self.range <= enemy.rect.centerx <= self.rect.centerx + self.range:
                if self.rect.centery - self.range <= enemy.rect.centery <= self.rect.centery + self.range:
                    return enemy
        return None
### TARGET FOR PROJECTILES FROM TOWERS ###
    def attack(self, target, projectile_group):
        projectile = Projectile(self.rect.centerx, self.rect.centery, target, self.damage)
        projectile_group.add(projectile)

### PROJECTILES CLASS ###
class Projectile(pg.sprite.Sprite):
    def __init__(self, x, y, target, damage):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))  # Adjust the size and appearance of the projectile
        self.image.fill(RED)  # Adjust the color of the projectile
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10  # Adjust the speed of the projectile
        self.target = target
        self.damage = damage

### PROJECTILE UPDATES ###
    def update(self):
        direction = self.calculate_direction()
        self.rect.x += direction[0] * self.speed
        self.rect.y += direction[1] * self.speed
        
### PROJECTILE COLLITION DETECTOR ###
        if pg.sprite.collide_rect(self, self.target):
            if self.target is not None:
                self.target.health -= self.damage
                if self.target.health <= 0:
                    self.target.kill()
                self.kill()
            else:
                self.kill()
### PROJECTILE DIRECTION MODIFIER ###
    def calculate_direction(self):
        dx = self.target.rect.centerx - self.rect.centerx
        dy = self.target.rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)
### PROJECTILE DISTANCE MODIFIER ###
        if distance != 0:
            direction_x = dx / distance
            direction_y = dy / distance
            return direction_x, direction_y

        return 0, 0