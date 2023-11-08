import pygame, sys
from random import randint

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 640, 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ballx = randint(0,400) 
bally = randint(0, 600)
vx = 2
vy = 2

while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ballx += vx
    bally += vy
    if ballx < 0 or ballx > WIDTH:
        vx = -vx
    if bally < 0 or bally > HEIGHT:
        vy = -vy
    #pygame.time.wait(10)
    pygame.draw.circle(screen, WHITE, (ballx, bally), 10)
    pygame.display.update()