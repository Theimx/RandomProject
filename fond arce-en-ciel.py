import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1350,629),pygame.RESIZABLE)
running = True
timer = pygame.time.Clock()
r,g,b = 0,0,0

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    r += 4
    g += 2
    b += 3
    if r >= 254:
        r = 0
    if g >= 254:
        g = 0
    if b >= 254:
        b = 0
    color = (r,g,b)
    screen.fill(color)
    pygame.display.update()
    timer.tick(60)
