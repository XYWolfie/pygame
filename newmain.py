import pygame as pg
from sprites import *

class Game():
    def __init__(self):
        pg.init()
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.PINK = (250,200,200)
        self.GREEN = 0,50,45

        self.WIDTH = 1500
        self.HEIGHT = 706
       
        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT))

        self.bg = pg.image.load("full bg.png").convert_alpha()
        self.bg = pg.transform.scale(self.bg, (2546, 706))
        self.bg_WIDTH = self.bg.get_width()

        self.ground = pg.image.load("long grass.png").convert_alpha()
        self.ground = pg.transform.scale(self.ground, (1550, 147))

        self.platform1 = pg.image.load("long platform1.png").convert_alpha()
        self.platform1 = pg.transform.scale(self.platform1, (100, 195))

        self.platform2 = pg.image.load("long platform2.png").convert_alpha()
        self.platform2 = pg.transform.scale(self.platform2, (100, 411))

        self.platform3 = pg.image.load("long platform3.png").convert_alpha()
        self.platform3 = pg.transform.scale(self.platform3, (100, 333))

        self.floatpiece = pg.image.load("floating piece.png").convert_alpha()
        self.floatpiece = pg.transform.scale(self.floatpiece, (150, 163))

        self.rock = pg.image.load("rock.png").convert_alpha()
        self.rock = pg.transform.scale(self.rock, (200, 87))

        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)

        self.FPS = 120
        self.clock = pg.time.Clock()

        pg.mixer.music.load('LOFI.rar') 
        pg.mixer.music.play(-1) 

        LOFI = pg.mixer.Sound("LOFI.rar") 
        LOFI.set_volume(0.5) 

        self.new()

    def new(self):

        self.redhood_group = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_enemies = pg.sprite.Group()
        self.all_traps = pg.sprite.Group()
        self.all_stilltraps = pg.sprite.Group()
        self.food = pg.sprite.Group()
        self.all_liveenemies = pg.sprite.Group()

        #self.blocks = pg.sprite.Group()

        #self.blocks.add(self.rock)

        self.redhood = Player(self)
        self.redhood_group.add(self.redhood)
    
        
    
        self.last_collision = 0

        self.text_font = self.comic_sans30.render(str(self.redhood.hp), False, (self.WHITE))

        self.run()

    def run(self):  
        i = 0           
        playing = True
        while playing:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False

            self.now =pg.time.get_ticks()


            #self.screen.fill((self.GREEN))
            self.screen.blit(self.bg, (i,0))
            self.screen.blit(self.bg,(self.bg_WIDTH+i,0))
            if (i == -self.bg_WIDTH):
                self.screen.blit(self.bg,(self.bg_WIDTH+i,0))
                i=0
            i-=1


            self.hits = pg.sprite.spritecollide(self.redhood, self.all_enemies, False)
            if self.hits:
                if self.last_collision < self.now - 750:
                    self.redhood.immune = False


                if not self.redhood.immune:
                    self.redhood.hp -= 50
                    self.redhood.immune = True
                    self.last_collision = self.now
                    self.text_font = self.comic_sans30.render(str(self.redhood.hp), False, (self.WHITE))
                    if self.redhood.hp <=0:
                        self.dead_frames = True
                        self.redhood.kill()
                        self.game_over_loop()

            
            #collision = pg.sprite.spritecollide(self.redhood, self.blocks, False)
            #if collision:
                #self.check_collision(collision[0])
          
            if len(self.all_traps) < 5:
                fireball = Trap(self)
                self.all_sprites.add(fireball)
                self.all_traps.add(fireball)
                self.all_enemies.add(fireball)

            

            

            

            self.screen.blit(self.text_font, (10, 10))
            self.screen.blit(self.rock, (350, 450))
            self.screen.blit(self.ground, (-20, 500))
            self.screen.blit(self.platform1, (1300, 0))
            self.screen.blit(self.platform2, (800, 0))
            self.screen.blit(self.platform3, (600, 0))
            self.screen.blit(self.floatpiece, (1050, 230))

            pg.mixer.Sound.play(self.LOFI)
            
        

            self.all_sprites.update()
        
            self.all_sprites.draw(self.screen)

            pg.display.update()

    #def check_collision(self, collided_block):
        #offset = self.redhood.speed + 1
        #top = collided_block.rect.bottom - self.redhood.rect.top
        #bottom = collided_block.rect.top - self.redhood.rect.bottom
 
        #if top < offset and top > -offset:
            #self.redhood.rect.top = collided_block.rect.bottom + 1
            #print("collision top")
        #elif bottom > -offset and bottom < offset:
            #self.redhood.rect.bottom = collided_block.rect.top -1
            #print("collision bottom")
        
        #left = collided_block.rect.right - self.redhood.rect.left
        #right = collided_block.rect.left - self.redhood.rect.right
 
        #if left < offset and left > -offset:
            #self.redhood.rect.left = collided_block.rect.right + 1
            #print("collision left")
        #elif right > -offset and right < offset:
            #self.redhood.rect.right = collided_block.rect.left - 1
            #print("collision right")
 
        self.redhood.pos.x = self.redhood.rect.centerx
        self.redhood.pos.y = self.redhood.rect.centery
    

    def game_over_loop(self):

        self.game_over = True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text=self.text_font = self.comic_sans30.render("Game Over, press R to restart", False, (self.WHITE))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.game_over = False

            self.screen.fill(self.BLACK)
            self.screen.blit(self.game_over_text, (30,30))
            pg.display.update()

        self.new()
            

g = Game() 