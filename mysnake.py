from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
flag=True

while flag==True:
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            flag = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_q:
            flag = False 

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()

 
pg.quit()    

## On ne peut pas quitter avec la croix car il n'est pas écrit dans le
## programme comment intéragir avec le clavier et la souris