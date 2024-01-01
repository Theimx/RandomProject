import random

coups = [ ]
rejouer = "oui"
while rejouer == "oui":
    tours = 0
    rep = 0
    nbA = random.randint(1, int(input("Quel est le nombre maximal que je peux te faire deviner: ")))
    while rep != nbA:
        rep = int(input("Fait un essaie pour trouver le nombre que j'ai en tête "))
        if nbA > rep:
            print("C'est plus")
        if nbA < rep:
            print("C'est moins")
        tours += 1
    print("Tu as gagné en " + str(tours) + " tours")
    coups.append(tours)
    print("Merci d'avoir joué à mon jeux! Ta moyenne de coups est de  " + str(sum(coups) / len(coups)) + " coups.")
    rejouer = input("Veux tu rejouer [oui/non]:  ")







#moyenne = 1+1+1+1/4
