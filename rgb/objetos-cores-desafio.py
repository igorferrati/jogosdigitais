import pygame
from pygame.locals import *
from sys import exit 
import random

pygame.init()

#retangulo
def rectangle_create(screen, color, x, y, width, height):
    surface = pygame.draw.rect(screen, color, (x, y, width, height))
    return surface

#circle
def circle_create(screen, color, x, y, radius):
    surface = pygame.draw.circle(screen, color, (x, y), radius)
    return surface

#postions
x1 = random.randint(0,800)
x2 = random.randint(0,800)
y2 = random.randint(0,800)
y1 = random.randint(0,600)

#size
width = random.randint(1,100)
height = random.randint(1,100)
radius = random.randint(1,50)

#screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Praticando A3")

#color
color_1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

color_2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    screen.fill((255, 255, 255))

    rectangle_create(screen, color_1, x1, y1, width, height)
    circle_create(screen, color_2, x2, y2, radius)

    #update screen
    pygame.display.update()