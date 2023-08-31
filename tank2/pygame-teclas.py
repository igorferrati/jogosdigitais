import pygame
from pygame.locals import *
from sys import exit
import math

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

tank = pygame.image.load('tank.jpg').convert()

tank_rect = tank.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))
tank_x =  tank_rect.width // 2
tank_y =  tank_rect.height //2

x,y=0,0
move_x, move_y = 0,0

rotation_angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_LEFT:
                move_x=-1
                rotation_angle =0
        if event.type == KEYUP:
            if event.key == K_LEFT:
                move_x=0
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move_x=+1
                rotation_angle =180
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                move_x=0
        if event.type ==  KEYDOWN:
            if event.key == K_UP:
                move_y=-1
                rotation_angle = 270
        if event.type == KEYUP:
            if event.key == K_UP:
                move_y=0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                move_y=+1
                rotation_angle = 90
        if event.type == KEYUP:
            if event.key == K_DOWN:
                move_y=0
            
        x += move_x
        y += move_y
        
        rotation_tank = pygame.transform.rotate(tank, rotation_angle)
        rotation_rect = rotation_tank.get_rect(center=tank_rect.center)
        rotation_rect_tec = rotation_rect.move(x, y)

        screen.fill((255,255,255))
        screen.blit(rotation_tank, rotation_rect_tec.topleft)

        pygame.display.update()