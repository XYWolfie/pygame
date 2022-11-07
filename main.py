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

    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= speed
    if keys[pg.K_s]:
        y += speed
    if keys[pg.K_d]:
        x += speed
    if keys[pg.K_a]:
        x -= speed

    if x > 700:
        x = 700
    if x < 0:
        x = 0

    if y > 500:
        y = 500
    if y < 0:
        y = 0

    
    box = pg.Rect(x,y, 100,100)
    pg.draw.rect(screen, WHITE, box)

    screen.blitt(player_img, (x,y))


    pg.display.update()
    
