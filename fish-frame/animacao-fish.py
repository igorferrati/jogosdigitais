import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Fish Animation')

WHITE = (255, 255, 255)

catImg = pygame.image.load('/home/igor/Desktop/docs/myprojects/jogosdigitais/fish-frame/magikarp.png')
#set image
catImg = pygame.transform.scale(catImg, (120, 120))

fishx = 10
fishy = 10
direction = 'right'

while True: # the main game loop

    if direction == 'right':
        fishx += 5
        if fishx == 280:
            direction = 'down'
    elif direction == 'down':
        fishy += 5
        if fishy == 180:
            direction = 'left'
    elif direction == 'left':
        fishx -= 5
        if fishx == 10:
            direction = 'up'
    elif direction == 'up':
        fishy -= 5
        if fishy == 10:
            direction = 'right'
            
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(catImg, (fishx, fishy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
