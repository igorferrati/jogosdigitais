import pygame, sys, math

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Mass Spring Damper System')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

delta_t = 0.1
m = 1
k = 1 #Spring Constant
c = 0.04 # 1.5 #Damper Constant

x = 0
y = 250

vx = 10
vy = 0

while True:
    #screen.fill(BLACK)

    fx = 0
    fy = -k * (y-150) -c * vy

    vx = vx + (fx / m) * delta_t
    vy = vy + (fy / m) * delta_t

    x = x + vx * delta_t
    y = y + vy * delta_t

    if x > 400:
        screen.fill(BLACK)
        x = 0
        
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)