import pygame as pg
from random import randint, choice
vec = pg.math.Vector2


player_img = pg.image.load("redhood.png")
player_img = pg.transform.scale(player_img, (32,62))

player_left_img = pg.transform.flip(player_img, True, False)

RUN0 = pg.image.load("redhood run0.png")
RUN0 = pg.transform.scale(RUN0,(32,62))
RUN1 = pg.image.load("redhood run1.png")
RUN1 = pg.transform.scale(RUN1,(32,62))
RUN2 = pg.image.load("redhood run2.png")
RUN2 = pg.transform.scale(RUN2,(32,62))
RUN3 = pg.image.load("redhood run3.png")
RUN3 = pg.transform.scale(RUN3,(32,62))
RUN4 = pg.image.load("redhood run4.png")
RUN4 = pg.transform.scale(RUN4,(32,62))
RUN5 = pg.image.load("redhood run5.png")
RUN5 = pg.transform.scale(RUN5,(32,62))
RUN6 = pg.image.load("redhood run6.png")
RUN6 = pg.transform.scale(RUN6,(32,62))
RUN7 = pg.image.load("redhood run7.png")
RUN7 = pg.transform.scale(RUN7,(32,62))
RUN8 = pg.image.load("redhood run8.png")
RUN8 = pg.transform.scale(RUN8,(32,62))
RUN9 = pg.image.load("redhood run9.png")
RUN9 = pg.transform.scale(RUN9,(32,62))
RUN10 = pg.image.load("redhood run10.png")
RUN10 = pg.transform.scale(RUN10,(32,62))

STANDING = pg.image.load("redhood.png")
STANDING = pg.transform.scale(STANDING,(32,62))
STANDING2 = pg.image.load("redhood.png")
STANDING2 = pg.transform.scale(STANDING2,(32,62))

JUMP1 = pg.image.load("redhood jump1.png")
JUMP1 = pg.transform.scale(JUMP1,(32,62))
JUMP2 = pg.image.load("redhood jump2.png")
JUMP2 = pg.transform.scale(JUMP2,(32,62))
JUMP3 = pg.image.load("redhood jump3.png")
JUMP3 = pg.transform.scale(JUMP3,(32,62))
JUMP4 = pg.image.load("redhood jump4.png")
JUMP4 = pg.transform.scale(JUMP4,(32,62))



running_frames = [RUN0, RUN1, RUN2, RUN3, RUN4, RUN5, RUN6, RUN7, RUN8, RUN9, RUN10]
standing_frames = [STANDING, STANDING2]
jumping_frames = [JUMP1, JUMP2, JUMP3, JUMP4]



class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.current_frame = 0   
        self.last_update = 0
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,500)
        self.rect.center = self.pos
        self.speed = 6
        self.hp = 500
        self.immune = False

        self.running = False
        self.left = True
        self.jumping = False
        self.jump = pg.time.get_ticks()
        self.jump_start = 0
        self.last_jump = 0
        self.falling = False


        self.projectile_speed = 5
        self.running_frames = running_frames
        self.image_left = player_left_img

    def attack(self):
        Ranged_attack(self.game, self.pos.x, self.pos.y, self.attack_direction_x, self.attack_direction_y)
 

    def update(self):
        self.animate()
        self.rect.center = self.pos
        self.standing = True
        self.running = False
        now = pg.time.get_ticks()

        
        
        keys =pg.key.get_pressed()
        if keys[pg.K_w]:
            #self.pos.y += 5
            self.pos.y -= self.speed
            self.running = False
            self.jumping = True
            self.jump_start = 0
        if keys[pg.K_s]:
            self.pos.y += self.speed
            self.running = True
        if keys[pg.K_a]:
            self.pos.x -= self.speed
         
            self.running = True
            self.left = False
        if keys[pg.K_d]:
            self.pos.x += self.speed
           
            self.running = True
            self.left = True

        if self.jumping:
            self.pos.y -= 5
            #self.pos.y -= self.speed
            #self.pos.y -= 5
            #self.jump_start += 1

        else:
            self.pos.y += 5

        if self.pos.y > 200:
            self.jumping = False
            self.falling = True

        if self.falling == True:
            self.pos.y += 5


        


        if self.jump_start > 20:
            self.jumping = False

        #if self.jumped:
            #if self.last_jump < self.game.now -2000:
                

        self.attack_direction_x, self.attack_direction_y = 0, 0

        if keys[pg.K_UP]:
            self.attack_direction_y = -self.projectile_speed
        if keys[pg.K_DOWN]:
            self.attack_direction_y = self.projectile_speed
        if keys[pg.K_LEFT]:
            self.attack_direction_x = -self.projectile_speed            
        if keys[pg.K_RIGHT]:
            self.attack_direction_x = self.projectile_speed

        if not self.attack_direction_x == 0 and self.attack_direction_y == 0:
            if keys[pg.K_SPACE]:
                self.attack()
        
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > 1600:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.y > 500:
            self.pos.y = 500
       
        
      
        self.rect.center = self.pos

    def animate(self):
        now = pg.time.get_ticks()

        if self.running:
            if now - self.last_update > 50:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.running_frames)
                self.image = self.running_frames[self.current_frame]
                self.rect = self.image.get_rect()
                

                if self.left:
                    self.image = pg.transform.flip(self.image, True, False)

            

        

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
            

fireball_img = pg.image.load("Fireball_68x9 1.png")
fireball_img = pg.transform.scale(fireball_img, (50,70))

class Trap(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = fireball_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(1600,1800),randint(0,500))
        self.rect.center = self.pos
        self.speed = 5





    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed

        if self.pos.x < -100:
            self.pos.x = randint(1500, 1800)
            self.pos.y = randint(0,500)