from random import randint
import pygame as pg

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (250,200,200)
color = (randint(0,255), randint(0,255), randint(0,255))

screen = pg.display.set_mode((800,600))

x = 50
y = 50

speed = 5
FPS = 120
clock = pg.time.Clock()

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False


    screen.fill(PINK)
    player_img = pg.image.load("Red_hood_1.png")
    player_img = pg.transform.scale(player_img, (300,320))

    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= speed
    if keys[pg.K_s]:
        y += speed
    if keys[pg.K_d]:
        x += speed
    if keys[pg.K_a]:
        x -= speed

    if x > 600:
        x = 600
    if x < -100:
        x = -100

    if y > 350:
        y = 350
    if y < -100:
        y = -100

    
    

    screen.blit(player_img, (x,y))


    pg.display.update()
    
