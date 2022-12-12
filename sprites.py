import pygame as pg
from random import randint, choice
vec = pg.math.Vector2


player_img = pg.image.load("Redhood.png")
player_img = pg.transform.scale(player_img, (40,70))

player_left_img = pg.transform.flip(player_img, True, False)




class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.current_frame = 0   
        self.last_update = 0
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 6
        self.hp = 500
        self.immune = False

        self.projectile_speed = 5

        self.image_left = player_left_img



    def update(self):

        self.rect.center = self.pos


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

        self.attack_direction_x, self.attack_direction_y = 0, 0

        if keys[pg.K_UP]:
            self.attack_direction_y = -self.projectile_speed
        if keys[pg.K_DOWN]:
            self.attack_direction_y = self.projectile_speed
        if keys[pg.K_LEFT]:
            self.attack_direction_x = -self.projectile_speed            
        if keys[pg.K_RIGHT]:
            self.attack_direction_x = self.projectile_speed

        
        
        self.rect.center = self.pos

        

        
            
enemy_img = pg.image.load("reaper.png")
enemy_img = pg.transform.scale(enemy_img, (50,70))


class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, game, x ,y, direction_x, direction_y):
        self.groups = game.all_sprites, game.projectiles_grp 
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface([50,50])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) 
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.rect.center = self.pos 


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