import pygame
pygame.init()

#but du programme : faire une liste qui contient 405 argument pour les 405 case de l'écrans
#les 405 valeur doivent être tout les multiple de 60 dans les deux sens de 900 (15*60) a 1620 (27*60)
#puis créé une boucle for qui blit toute ces valeurs avec le moins de ligne de code possible




coordonné = [(0,0)]

b = 0
for i in range(25):
    b += 60
    coordonné.append((b,0))
b = 0
for h in range(26):
    coordonné.append((b,60))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,120))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,180))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,240))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,300))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,360))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,420))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,480))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,540))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,600))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,660))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,720))
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,780))
    b += 60




#faire une boucle for pour chaque ligne (pas collone )


