import pygame as pg
from sprites import *

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (250,200,200)
GREEN = 0,50,45

WIDTH = 1000
HEIGHT = 1000

redhood_group = pg.sprite.Group()
all_sprites = pg.sprite.Group()
all_enemies = pg.sprite.Group()
all_traps = pg.sprite.Group()
all_stilltraps = pg.sprite.Group()

redhood = Player()
redhood_group.add(redhood)
reaper = Enemy()
all_enemies.add(reaper)
spiketrap = Trap()
all_stilltraps.add(spiketrap)
fireball = Trap()
all_traps.add(fireball)
all_sprites.add(redhood, reaper, spiketrap, fireball)



screen = pg.display.set_mode((WIDTH,HEIGHT))

FPS = 120
clock = pg.time.Clock()



comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
 
print(redhood.life)

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False



    screen.fill(GREEN)

    hits = pg.sprite.spritecollide(reaper,redhood_group, True)
    

    if len(all_enemies) < 2:
        reaper = Enemy()
        all_sprites.add(reaper)
        all_enemies.add(reaper)
    if hits:
        redhood.life -= 10 
        

    hits = pg.sprite.spritecollide(fireball,redhood_group, True)
    

    if len(all_traps) < 20:
        fireball = Trap()
        all_sprites.add(fireball)
        all_traps.add(fireball)
    if hits:
        redhood.life -= 10 
        

    hits = pg.sprite.spritecollide(spiketrap,redhood_group, True)
       

    if len(all_stilltraps) < 20:
        spiketrap = Stilltrap()
        all_sprites.add(spiketrap)
        all_stilltraps.add(spiketrap)
    if hits:
        redhood.life -= 10  
       
         

    hits = pg.sprite.spritecollide(redhood, all_enemies, True)
            

    text_player_hp = comic_sans30.render(str(redhood.life), False, (WHITE))

    screen.blit(text_player_hp, (10, 10))


    all_sprites.update()
   
    all_sprites.draw(screen)

    pg.display.update() 
