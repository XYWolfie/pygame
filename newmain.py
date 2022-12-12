import pygame as pg
from sprites import *

class Game():
    def __init__(self):
        pg.init()
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.PINK = (250,200,200)
        self.GREEN = 0,50,45

        self.WIDTH = 2546
        self.HEIGHT = 706
       
        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT))

        self.bg = pg.image.load("full bg.png").convert_alpha()
        self.bg = pg.transform.scale(self.bg, (2546, 706))

        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)

        self.FPS = 120
        self.clock = pg.time.Clock()

        self.new()

    def new(self):

        self.redhood_group = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.all_enemies = pg.sprite.Group()
        self.all_traps = pg.sprite.Group()
        self.all_stilltraps = pg.sprite.Group()
        self.food = pg.sprite.Group()
        self.all_liveenemies = pg.sprite.Group()

        self.redhood = Player(self)
        self.redhood_group.add(self.redhood)
    
        self.grapesoda = Food()
        self.food.add(self.grapesoda)
        self.all_sprites.add(self.redhood, self.grapesoda)
    
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


            self.screen.fill((self.GREEN))
            self.screen.blit(self.bg, (i,0))
            self.screen.blit(self.bg,(self.WIDTH+i,0))
            if (i == -self.WIDTH):
                self.screen.blit(self.bg,(self.WIDTH+i,0))
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

            self.hits = pg.sprite.spritecollide(self.redhood, self.food, True)
            if self.hits:
                self.redhood.hp +=100

            if len(self.food) < 1:
                grapesoda = Food()
                self.all_sprites.add(grapesoda)
                self.food.add(grapesoda)

            if len(self.all_liveenemies) < 1:
                reaper = Liveenemy(self)
                self.all_sprites.add(reaper)
                self.all_enemies.add(reaper)
                self.all_liveenemies.add(reaper)

            if len(self.all_traps) < 20:
                fireball = Trap()
                self.all_sprites.add(fireball)
                self.all_traps.add(fireball)
                self.all_enemies.add(fireball)

            

            

            self.screen.blit(self.text_font, (10, 10))


            self.all_sprites.update()
        
            self.all_sprites.draw(self.screen)

            pg.display.update()

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