import math
import pygame
from pygame.locals import *
from random import randint 

class Asteroid:
    def __init__(self , x, y, raio, acceleration_x, acceleration_y):
        self.x = x
        self.y = y
        self.raio = raio
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y


def colisao(ast1, ast2):
    distancia =  math.sqrt( ((ast1.x-ast2.x)**2)+((ast1.y-ast2.y)**2) )
    print('distancia: ', distancia)
    if (ast1.raio + ast2.raio) >= distancia:
        return True
    else:
        return False

size = [20, 5, 10]
colorAsteroid = [(186,85,211),(245,222,179),(248,248,255)]

asteroids = [
    Asteroid(randint(10,590), randint(10, 390), size[i%3], randint(-1,1), randint(-1,1)) for i in range(10)
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

    #drawing asteroids
    for i, ateroid in enumerate(asteroids):
        pygame.draw.circle(screen, colorAsteroid[i%3], (asteroids[i].x, asteroids[i].y), asteroids[i].raio)

    pygame.display.flip()

    clock.tick(60)
