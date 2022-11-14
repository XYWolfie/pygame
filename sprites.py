import pygame as pg
from random import randint
vec = pg.math.Vector2

bg_img = pg.image.load("bg_img.png")
bg_img = pg.transform.scale(bg_img,(1000,1000))


player_img = pg.image.load("Redhood.png")
player_img = pg.transform.scale(player_img, (40,70))

player_left_img = pg.transform.flip(player_img, True, False)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 6
        
        self.life = 50

        self.image_left = player_left_img

    

    def update(self):

        keys =pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.image = player_img
        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = player_left_img

       
        self.rect.center = self.pos

        self.move_to = vec(pg.mouse.get_pos()) 
        self.move_vector = self.move_to - self.pos  
        self.pos += self.move_vector.normalize() * self.speed  
            
        
        

enemy_img = pg.image.load("reaper.png")
enemy_img = pg.transform.scale(enemy_img, (50,70))

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(0,1100), 500)
        self.rect.center = self.pos
        self.speed = 5

    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed

        if self.pos.x == randint(0,1000):
            self.pos.y <= -100
            self.pos.y >= 1100

spiketrap_img = pg.image.load("Spike Trap 1 A.png")
spiketrap_img = pg.transform.scale(spiketrap_img, (30,30))

class Stilltrap(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = spiketrap_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(0,1000),randint(0,1000))
        self.rect.center = self.pos

fireball_img = pg.image.load("Fireball_68x9 1.png")
fireball_img = pg.transform.scale(fireball_img, (50,70))

class Trap(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = fireball_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(500,1500),randint(0,1100))
        self.rect.center = self.pos
        self.speed = 5

    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed

        if self.pos.x < -100:
            self.pos.x = 950
            self.pos.y = randint(0,1100)