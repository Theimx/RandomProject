import pygame
pygame.init()

screen = pygame.display.set_mode((1350,629),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

largeur_edurance = 300
while running == True:
    clock.tick(100)
    pygame.display.update()
    screen.fill((20, 255, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.draw.rect(screen, "White", [500, 300, largeur_edurance, 40])


    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        if largeur_edurance > 1:
            largeur_edurance -= 1

    if pressed[pygame.K_RIGHT]:
        if largeur_edurance < 300:
            largeur_edurance += 1
