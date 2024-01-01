import pygame
pygame.init()

screen = pygame.display.set_mode((1350,629),pygame.RESIZABLE)
running = True
clock = pygame.time.Clock()
nombres = 0


color = (0,255,0)
smallfont = pygame.font.SysFont('Corbel',35)



while running == True:
    pygame.display.flip()

    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nombres += 1
                print(pygame.mouse.get_pos(),str(nombres))

                text = smallfont.render(str(pygame.mouse.get_pos()), True, color)
                screen.blit(text, (pygame.mouse.get_pos()))