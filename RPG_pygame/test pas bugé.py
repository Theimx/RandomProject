import pygame, random, time
pygame.init()


from Gui import gui_on
from liste_coordonnées import coordonné


screen = pygame.display.set_mode((1350,629),pygame.RESIZABLE)
logo = pygame.image.load("demo/logo.png").convert()
pygame.display.set_caption("Netige Studio")
pygame.display.set_icon(logo)
speed = 12
x = 0
y = 0
sprite = pygame.image.load("demo/bas.png")
bas = pygame.image.load("demo/bas.png")
haut = pygame.image.load("demo/haut.png")
droite = pygame.image.load("demo/droite.png")
gauche = pygame.image.load("demo/gauche.png")
grass = pygame.image.load("demo/grass.png").convert()

clock = pygame.time.Clock()
runing = True
largeur_edurance = 150
colorj = (0,255,0)



#--Echap menu ----------
color = (0,0,0)
color_light = (170,170,170)
color_dark = (100,100,100)

smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('Quitter' , True , color)
#-----------------------



direction = "BAS"
pressed = pygame.key.get_pressed()


def jauge_vie():
    global largeur_edurance,colorj,pressed


    pygame.draw.rect(screen, colorj, [(x-25), (y-50), largeur_edurance, 30])
    pygame.draw.rect(screen, "Black", [(x - 25), (y - 50), 150, 31],2)
    if largeur_edurance >= 150:
        colorj = "Yellow"
    if largeur_edurance < 150 and largeur_edurance > 100:
        colorj = "Green"
    if largeur_edurance < 100:
        colorj = "Orange"
    if largeur_edurance < 25:
        colorj = "Red"


    if pressed[pygame.K_m]:
        if largeur_edurance > 1:
            largeur_edurance -= 1
        else:
            respawn()
            largeur_edurance += 150


    if pressed[pygame.K_p]:
        if largeur_edurance < 150:
            largeur_edurance += 1

def FPS():

    def Render_Text(what, color, where):
        font = pygame.font.SysFont('Corbel', 35)
        text = font.render(what, True, pygame.Color(color))
        screen.blit(text,where)

    Render_Text(str(int(clock.get_fps()))+" FPS", (0,0,255), (0,0))



def respawn():

    global x,y
    x = 650
    y = 315


def gui():
    global gui_on

    if gui_on == True:
        pygame.draw.rect(screen, (211, 211, 211), [345, 100, 900, 600])
        pygame.draw.rect(screen, "Black", [345, 100, 900, 600],10)



        if 500 <= mouse[0] <= 500 + 600 and 600 <= mouse[1] <= 600 + 40:
            pygame.draw.rect(screen, color_light, [500, 600, 600, 40])

        else:
            pygame.draw.rect(screen, color_dark, [500, 600, 600, 40])

        screen.blit(text, (725, 605))
        if event.type == pygame.MOUSEBUTTONDOWN:

            if 500 <= mouse[0] <= 500 + 600 and 600 <= mouse[1] <= 600 + 40:
                if gui_on == True:
                    pygame.quit()
        pygame.draw.rect(screen, 'Black', [500, 600, 600, 40],3)

def mouvement():

    global bas , haut ,droite,gauche,direction,speed,x,y,sprite

    if direction == "GAUCHE":
        x -= speed
        sprite = gauche

    if direction == "DROITE":
        x += speed
        sprite = droite

    if direction == "BAS":
        y += speed
        sprite = bas

    if direction == "HAUT":
        y -= speed
        sprite = haut



NB_COL = 27
NB_ROW = 15
CELL_SIZE = 60
grille_combat = False
def show_grid():
    
    if grille_combat == True:
        for i in range(0,NB_COL):
            for j in range(0,NB_ROW):
                rect = pygame.Rect(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE)
                pygame.draw.rect(screen,'Black',rect, width=1)


def show_grass():
   for i in coordonné:
      screen.blit(grass,i)
      




while runing == True:


    clock.tick(30)

    screen.fill((255,255,255))
    show_grass()
    show_grid()
    screen.blit(sprite,(x,y))
    jauge_vie()
    FPS()
    gui()
    pygame.display.update()


    mouse = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()
    size_screen = screen.get_size()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if gui_on == False:
                    gui_on = True
                else:
                    gui_on = False

            if event.key == pygame.K_a:
                if grille_combat == False :
                    grille_combat = True 
                else:
                    grille_combat = False 
                    

    if pressed[pygame.K_LEFT] or pressed[pygame.K_q]:
        direction = "GAUCHE"
        mouvement()
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        direction = "DROITE"
        mouvement()
    if pressed[pygame.K_UP] or pressed[pygame.K_z]:
        direction = "HAUT"
        mouvement()
    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        direction = "BAS"
        mouvement()

    if pressed[pygame.K_t]:
        respawn()

