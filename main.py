import pygame
from snake import Snake
from apple import Apple
import os.path
import time

filepath = os.path.dirname(__file__)

pygame.init()

running = True

#Lil JSON
SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
pygame.display.set_icon(pygame.image.load(os.path.join(filepath,'apple.png')))
pygame.display.set_caption("Snake 0.1")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
font = pygame.font.SysFont("comicsansms", 12)


snk = Snake()
ap = Apple()
score = 0
i = 0
GAME_OVER = False

while running:
    #SCREEN REFRESH
    screen.fill((0,0,0))


    #EVENT CHECKER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snk.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                snk.direction = 'right'
            elif event.key == pygame.K_UP:
                snk.direction = 'up'
            elif event.key == pygame.K_DOWN:
                snk.direction = 'down'
    
    if snk.Is_Crashing():
        screen.blit(font.render('GAME OVER', True, (0, 128, 0)),(400-30,300))
        pygame.display.update()
        pygame.time.wait(1000)
        score = 0
        snk.Restart_Snake()
        ap.Eaten()

    ap.Draw_apple(screen)

    #SNAKE THG    
    snk.Draw_snake(screen)
    if i == 100:
        snk.Ruch() 
        i = 0
        if ap.coordinates == snk.head_coordinates:
            snk.Grow()
            ap.Eaten()
            score += 1

    screen.blit(font.render(str(score), True, (0, 128, 0)),(10,10))
    #UPDATE
    pygame.display.update()
    i +=1