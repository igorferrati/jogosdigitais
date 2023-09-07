import pygame
from pygame.locals import *
from sys import exit 
import random

pygame.init()

#postions
x = random.randint(0,800)
y = random.randint(0,800)

#size
a_size = random.randint(1,100)
b_size = random.randint(1,100)

#screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Praticando A3")

#color
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    screen.fill(WHITE)
    #drawing
    pygame.draw.rect(screen, BLACK, [x, y, a_size, b_size])
    pygame.draw.circle(screen, RED, [x, y], a_size)
    #pygame.draw.(screen, RED, [x, y, 50, 50])

    #update screen
    pygame.display.update()