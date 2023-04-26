import pygame
from random import randrange

res=800
size=50

x,y=randrange(0,res,size),randrange(0,res,size)
apple=randrange(0,res,size),randrange(0,res,size)
dirs={'W':True,'S':True,'A':True,'D':True,}
length=1
snake=[(x,y)]
dx,dy=0,0
score=0
fps=60
speed_count,snake_speed=0,10

pygame.init()
pygame.display.set_caption("snake")
sc=pygame.display.set_mode([res,res])
clock=pygame.time.Clock()
font_sc=pygame.font.SysFont('Arial',26,bold=True)
font_end=pygame.font.SysFont('Arial',66,bold=True)
img=pygame.image.load('images/1.png')

def close_game():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

while True:
    sc.blit(img,(0,0))
    [(pygame.draw.rect(sc,pygame.Color('green'),(i,j,size-2,size-2)))for i,j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, size, size))

    render_sc=font_sc.render(f'score:{score}',1,pygame.Color('orange'))
    sc.blit(render_sc,(5,5))

    speed_count+=1
    if not speed_count%snake_speed:
        x+=dx*size
        y+=dy*size
        snake.append((x,y))
        snake=snake[-length:]

    if snake[-1]==apple:
        apple=randrange(size,res,size),randrange(size,res,size)
        length+=1
        score+=1
        snake_speed-=0
        snake_speed=max(snake_speed,4)

    if x<0 or x>res-size or y<0 or y>res-size or len(snake)!=len(set(snake)):
        while True:
            render_end=font_end.render('GAME OVER',1,pygame.Color('orange'))
            sc.blit(render_end,(res//2-200,res//3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)
    close_game()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }



