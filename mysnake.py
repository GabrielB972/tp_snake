from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
flag=True

def draw_board():
    for i in range(30):
        for j in range(15):
            if i%2==0:
                x,y=i*20,j*40
                width,height=20,20
                color=(255,255,255)
                rect = pg.Rect(x,y,width,height)
                pg.draw.rect(screen,color,rect)
            else :
                x,y=i*20,j*40+20 #pour les colonnes impaires on décale d'une case vesr le bas les blanches d'oùle +20
                width,height=20,20
                color=(255,255,255)
                rect = pg.Rect(x,y,width,height)
                pg.draw.rect(screen,color,rect)

def draw_snake(snake):
    for (x,y) in snake :
        color=(255,0,0)
        rect= pg.Rect(x*20,y*20,20,20)
        pg.draw.rect(screen,color,rect)

SNAKE = [
   (10, 15),
   (11, 15),
   (12, 15),
]

while flag==True:
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            flag = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_q:
            flag = False 
    draw_board()
    draw_snake(SNAKE)
    pg.display.update()
pg.quit()    

## On ne peut pas quitter avec la croix car il n'est pas écrit dans le
## programme comment intéragir avec le clavier et la souris