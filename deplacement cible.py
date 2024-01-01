import pygame
pygame.init()

pygame.display.set_caption("New Game")
screen = pygame.display.set_mode((1080, 720),pygame.RESIZABLE)
running = True


clock = pygame.time.Clock()
y,x = 0,0
orientation = "bas"


def deplacement():
   global orientation,y,x

   if orientation == "gauche":
      y -= 2
   if orientation == "droite":
      y += 2
   if orientation == "haut":
      x -= 2
   if orientation == "bas":
      x += 2




while running:



   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         pygame.quit()
         print("Fermeture du jeu")

   clock.tick(60)
   screen.fill("Black")
   pygame.draw.circle(screen,"Red",(y,x),20,5)
   pygame.display.flip()

   mouse = pygame.mouse.get_pos()
   pressed = pygame.key.get_pressed()


   if pressed[pygame.K_LEFT]:
      orientation = "gauche"
      deplacement()
   if pressed[pygame.K_RIGHT]:
      orientation = "droite"
      deplacement()
   if pressed[pygame.K_DOWN]:
      orientation = "bas"
      deplacement()
   if pressed[pygame.K_UP]:
      orientation = "haut"
      deplacement()
