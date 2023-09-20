import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

#set screen
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Fish Animation')
#background
WHITE = (255, 255, 255)

#load images
magikarpImg = pygame.image.load('/home/igor/Desktop/docs/myprojects/jogosdigitais/fish-frame/magikarp.png')
goldeenImg = pygame.image.load('/home/igor/Desktop/docs/myprojects/jogosdigitais/fish-frame/goldeen.png')
bubbleImg = pygame.image.load('/home/igor/Desktop/docs/myprojects/jogosdigitais/fish-frame/bubble.png')

#set size images
magikarpImg = pygame.transform.scale(magikarpImg, (120, 120))
goldeenImg = pygame.transform.scale(goldeenImg, (120, 120))
bubbleImg = pygame.transform.scale(bubbleImg, (25, 25))

#start positions
goldeenx = 10
goldeeny = 10
magikarpx = 200
magikarpy = 200
bubble1_x = 100
bubble1_y = 300
bubble2_x = 135
bubble2_y = 190

#star directions
goldeen_direction = 'right'
goldeen_vertical_direction = 'down'
magikarp_direction = 'left'
magikarp_vertical_direction = 'up'
bubble1_vertical_direction = 'up'
bubble2_vertical_direction = 'up'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Goldeen move
    if goldeen_direction == 'right':
        goldeenx += 4
        if goldeenx >= 280:
            goldeen_direction = 'left'
            goldeenImg = pygame.transform.flip(goldeenImg, True, False)  #flip horizontally
    else:
        goldeenx -= 4
        if goldeenx <= 10:
            goldeen_direction = 'right'
            goldeenImg = pygame.transform.flip(goldeenImg, True, False)

    if magikarp_vertical_direction == 'up':
        magikarpy -= 1
        if magikarpy <= 10:
            magikarp_vertical_direction = 'down'
    else:
        magikarpy += 1
        if magikarpy >= 200:
            magikarp_vertical_direction = 'up'


    #Magikarp move
    if magikarp_direction == 'left':
        magikarpx -= 4
        if magikarpx <= 10:
            magikarp_direction = 'right'
            magikarpImg = pygame.transform.flip(magikarpImg, True, False)  
    else:
        magikarpx += 4
        if magikarpx >= 280:
            magikarp_direction = 'left'
            magikarpImg = pygame.transform.flip(magikarpImg, True, False)  

    if goldeen_vertical_direction == 'down':
        goldeeny += 1
        if goldeeny >= 200:
            goldeen_vertical_direction = 'up'
    else:
        goldeeny -= 1
        if goldeeny <= 10:
            goldeen_vertical_direction = 'down'

    #bubbles move
    if bubble1_vertical_direction == 'up':
        bubble1_y -= 2
        if bubble1_y <= 0:
            bubble1_y = 300

    if bubble1_vertical_direction == 'up':
        bubble2_y -= 2
        if bubble2_y <= 0:
            bubble2_y = 300


    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(magikarpImg, (magikarpx, magikarpy))
    DISPLAYSURF.blit(goldeenImg, (goldeenx, goldeeny))
    DISPLAYSURF.blit(bubbleImg, (bubble1_x, bubble1_y))
    DISPLAYSURF.blit(bubbleImg, (bubble2_x, bubble2_y))

    pygame.display.update()
    fpsClock.tick(FPS)
