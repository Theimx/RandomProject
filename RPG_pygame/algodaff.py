import pygame , random 
pygame.init()

#le but de se fichier est de : 
#crée un sys d'affichage optimisé qui n'affiche que les blocks a affiché a l'écrans 
#definir plusieurs blocks de sol et crée une map de test 

CELL_SIZE = 60
NB_COL = 27
NB_ROW = 16

def show_grid():
    for i in range(0,NB_COL):
        for j in range(0,NB_ROW):
            rect = pygame.Rect(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,'Black',rect, width=2)



        

    



pygame.display.set_caption("affichage")
screen = pygame.display.set_mode((1080, 720),pygame.RESIZABLE)
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)     

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")


    screen.fill("White")
    show_grid()

    pygame.display.flip()












