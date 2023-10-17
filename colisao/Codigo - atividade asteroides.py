import math
import pygame
from pygame.locals import *
from random import randint 

class Asteroid:
    def __init__(self , x, y, raio, acceleration_x, acceleration_y, color):
        self.x = x
        self.y = y
        self.raio = raio
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.color = color


def colisao(ast1, ast2):
    distancia =  math.sqrt( ((ast1.x-ast2.x)**2)+((ast1.y-ast2.y)**2) )
    # print('distancia: ', distancia)
    if (ast1.raio + ast2.raio) >= distancia:
        return True
    else:
        return False

size = [20, 5, 10]
colorAsteroid = [(186,85,211),(245,222,179),(248,248,255)]

asteroids = [
    Asteroid(randint(10,590), randint(10, 390), size[i%3], randint(1,2), randint(1,2), colorAsteroid[i%3]) for i in range(10)
]

pygame.init()
screen = pygame.display.set_mode((600,400))
screen.fill((0, 0, 0))
pygame.display.set_caption('* A S T E R O I D S *')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    for asteroid in asteroids:
        asteroid.x += asteroid.acceleration_x
        asteroid.y += asteroid.acceleration_y

        if asteroid.x < 0 or asteroid.x > 600:
            asteroid.acceleration_x = -asteroid.acceleration_x #mult -1
        if asteroid.y < 0 or asteroid.y > 400:
            asteroid.acceleration_y = -asteroid.acceleration_y 
    
    screen.fill((0,0,0))

    #collision
    removed_asteroids = []
    
    for index1, asteroid1 in enumerate(asteroids):
        for index2, asteroid2 in enumerate(asteroids):
            if index1 != index2 and colisao(asteroid1, asteroid2):
                asteroid1.color = (255,0,0)
                asteroid2.color = (255,0,0)
                if asteroid1 not in removed_asteroids:
                    removed_asteroids.append(asteroid1)
                if asteroid2 not in removed_asteroids:
                    removed_asteroids.append(asteroid2)
    
    #remove to asteroids list
    for asteroid in removed_asteroids:
        asteroids.remove(asteroid)
        
    #drawing asteroids
    for i, ateroid in enumerate(asteroids):
        pygame.draw.circle(screen, asteroids[i].color, (asteroids[i].x, asteroids[i].y), asteroids[i].raio)

    pygame.display.flip()

    clock.tick(50)
