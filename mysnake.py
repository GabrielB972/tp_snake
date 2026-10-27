from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
flag=True
SNAKE = [
   (10, 15),
   (11, 15),
   (12, 15),
]
DIRECTION = (1, 0)
def draw_board():
    screen.fill((0,0,0))
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
               
    return            

def draw_snake(snake):
    for (x,y) in snake :
        color=(255,0,0)
        rect= pg.Rect(x*20,y*20,20,20)
        pg.draw.rect(screen,color,rect)
    return    

def move_snake(snake,direction):
    (dx,dy)=direction
    snake.pop(0)
    (x,y)=snake[-1]
    snake.append((x+dx,y+dy))
    return   





while flag==True:
    clock.tick(2)

    for event in pg.event.get():
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_UP and DIRECTION!=(0,1):
                DIRECTION=(0,-1)
            elif event.key==pg.K_DOWN and DIRECTION!=(0,-1):
                DIRECTION=(0,1)
            elif event.key==pg.K_RIGHT and DIRECTION!=(-1,0):
                DIRECTION=(1,0)
            elif event.key==pg.K_LEFT and DIRECTION!=(1,0):
                DIRECTION=(-1,0)            
        if event.type == pg.QUIT:
            flag = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_q:
            flag = False 
    draw_board()
    move_snake(SNAKE,DIRECTION)
    draw_snake(SNAKE) 
    print(SNAKE)
    pg.display.update()
pg.quit()    

## On ne peut pas quitter avec la croix car il n'est pas écrit dans le
## programme comment intéragir avec le clavier et la souris
##Le serpent ne s'arrête pas au bord 