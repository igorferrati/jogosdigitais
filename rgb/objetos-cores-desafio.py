import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

# Inicializa as cores dos retângulos
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Inicializa as cores dos retângulos com cópias das cores originais
current_colors = list(colors)

lerp_factor = 0.0
lerp_speed = 0.005

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    x, y = pygame.mouse.get_pos()

    # Desenha os 6 retângulos com as cores atualizadas
    for i in range(len(current_colors)):
        pygame.draw.rect(screen, current_colors[i], (0, i * 80, 640, 80))

    # Se o botão esquerdo do mouse for pressionado
    if pygame.mouse.get_pressed()[0]:
        for i in range(len(current_colors)):
            if y >= i * 80 and y < (i + 1) * 80:
                t = x / 640  # Normaliza a posição do mouse
                current_colors[i] = (int(t * colors[i][0]), int(t * colors[i][1]), int(t * colors[i][2]))

    pygame.display.update()
