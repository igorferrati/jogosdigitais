import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#tela
screen = pygame.display.set_mode((640, 480))

# define cores
original_colors = [(255, 0, 0), (0, 140, 0), (0, 90, 255),
                   (255, 255, 0), (255, 20, 255), (0, 100, 255)]

# Inicializa as cores dos retângulos copiando cores originais
current_colors = list(original_colors)

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

    # Se mouse for pressionado
    if pygame.mouse.get_pressed()[0]:
        for i in range(len(current_colors)):
            if y >= i * 80 and y < (i + 1) * 80:
                # Use as coordenadas do mouse para calcular a variação
                r_variation = int((x / 640) * 255)
                g_variation = int((y / 480) * 255)
                
                # Use a cor original como base e aplique a variação
                original_r, original_g, original_b = original_colors[i]
                r = (original_r + r_variation) % 256
                g = (original_g + g_variation) % 256
                current_colors[i] = (r, g, original_b)

    # Atualiza o título da janela
    color_str = ", ".join([str(c) for c in current_colors])
    pygame.display.set_caption("Cores: " + color_str)

    pygame.display.update()
