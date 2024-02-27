import pygame, random
pygame.init()

from liste_coordonnées import coordonné

pygame.display.set_caption("New Game")
screen = pygame.display.set_mode((1350, 629),pygame.RESIZABLE)
running = True
clock = pygame.time.Clock()

grass = pygame.image.load("demo/grass.grass.png").convert()



NB_COL = 27
NB_ROW = 13
CELL_SIZE = 60


def FPS():

   def Render_Text(what, color, where):
      font = pygame.font.SysFont('Corbel', 35)
      text = font.render(what, True, pygame.Color(color))
      screen.blit(text, where)

   Render_Text(str(int(clock.get_fps())) + " FPS", (0, 0, 0), (0, 0))



def show_grid():
    for i in range(0,NB_COL):
        for j in range(0,NB_ROW):
            rect = pygame.Rect(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,"Blue",rect, width=2)

def show_grass():
   global grass
   for i in coordonné:
      screen.blit(grass,i)
      degré = [90,180,270]
      valeur = random.choice(degré)
      grass = pygame.transform.rotate(grass,valeur)

while running:
   clock.tick(1)
   screen.fill((255,255,255))

   show_grass()
   show_grid()
      
   FPS()



   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         pygame.quit()
         print("Fermeture du jeu")



   pygame.display.flip()