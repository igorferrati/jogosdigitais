import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

# Dimensões da tela
screen = pygame.display.set_mode((640, 480), 0, 32)

# Defina as cores para cada retângulo (RGB)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    screen.fill((0, 0, 0))  # Preenche a tela com preto

    pygame.draw.rect(screen, colors[0], (0, 80, 640, 80))
    pygame.draw.rect(screen, colors[1], (0, 160, 640, 80))
    pygame.draw.rect(screen, colors[2], (0, 240, 640, 80))
    pygame.draw.rect(screen, colors[3], (0, 320, 640, 80))
    pygame.draw.rect(screen, colors[4], (0, 400, 640, 80))
    pygame.draw.rect(screen, colors[5], (0, 480, 640, 80))

    pygame.display.update()
