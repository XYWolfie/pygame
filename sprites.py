import pygame as pg
from random import randint, choice
vec = pg.math.Vector2


player_img = pg.image.load("Redhood.png")
player_img = pg.transform.scale(player_img, (40,70))

player_left_img = pg.transform.flip(player_img, True, False)

DEAD1 = pg.image.load('redhood 1dead.png')
DEAD2 = pg.image.load('redhood dead.png')


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0   
        self.last_update = 0
        self.standing = True    
        self.running = False
        self.jumping = False
        self.dead = False 
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 6
        self.hp = 500
        self.immune = False

        self.image_left = player_left_img

        self.dead_frames = [DEAD1, DEAD2]

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

        self.animate()

    def animate(self):
        self.now = pg.time.get_ticks()
        

        if self.dead:   
            if self.now - self.last_update > 350:   
                self.last_update = self.now
                self.current_frame = (self.current_frame + 1) % len(self.dead_frames)
                self.image = self.dead_frames[self.current_frame]
                self.rect = self.image.get_rect()
            
enemy_img = pg.image.load("reaper.png")
enemy_img = pg.transform.scale(enemy_img, (50,70))

class Liveenemy(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.pos = vec(self.game.redhood.pos.x, 800)
        self.rect.center = self.pos
        self.speed = 5
        self.immune = False
        self.direction_x = choice([-1, 1])
        self.direction_y = choice([-1, 1])

    def update(self):
        self.rect.center = self.pos

        self.pos.y -= self.speed

        if self.pos.y < -100:
            self.kill()

spiketrap_img = pg.image.load("Spike Trap 1 A.png")
spiketrap_img = pg.transform.scale(spiketrap_img, (30,30))

class Stilltrap(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = spiketrap_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(0,1000),randint(0,800))
        self.rect.center = self.pos

fireball_img = pg.image.load("Fireball_68x9 1.png")
fireball_img = pg.transform.scale(fireball_img, (50,70))

class Trap(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = fireball_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(1100,1500),randint(0,900))
        self.rect.center = self.pos
        self.speed = 5

    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed

        if self.pos.x < -100:
            self.pos.x = 950
            self.pos.y = randint(0,900)

grapesoda_img = pg.image.load("grape_soda.png")
grapesoda_img = pg.transform.scale(grapesoda_img, (30,50))

class Food(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = grapesoda_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(500,1500),randint(0,900))
        self.rect.center = self.pos
        self.speed = 5

    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed

        if self.pos.x < -100:
            self.pos.x = 950
            self.pos.y = randint(0,900)