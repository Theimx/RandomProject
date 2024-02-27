import random 
#but du programme : faire une liste qui contient 405 argument pour les 405 case de l'écrans
#les 405 valeur doivent être tout les multiple de 60 dans les deux sens de 900 (15*60) a 1620 (27*60)
#puis créé une boucle for qui blit toute ces valeurs avec le moins de ligne de code possible




coordonné = [(0,0)]
orientation = random.choice(90,180,270)

b = 0
for h in range(26):
    b += 60
    coordonné.append((b,0))
    coordonné.append(orientation)

b = 0
for h in range(26):
    coordonné.append((b,60))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,120))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,180))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,240))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,300))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,360))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,420))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,480))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,540))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,600))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,660))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,720))
    coordonné.append(orientation)
    b += 60

b = 0
for h in range(26):
    coordonné.append((b,780))
    coordonné.append(orientation)
    b += 60


print(coordonné)

#faire une boucle for pour chaque ligne (pas collone )


