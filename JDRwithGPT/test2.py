import random

class Donjon:
    def __init__(self, nom, monstres=None, tresors=None, boss=None, geo_terrain=None):
        self.nom = nom
        self.salles = []
        self.monstres = monstres if monstres is not None else []
        self.tresors = tresors if tresors is not None else []
        self.boss = boss if boss is not None else []
        self.geo_terrain = geo_terrain

    def ajouter_salle(self, salle):
        self.salles.append(salle)

    def ajouter_monstre(self, monstre):
        self.monstres.append(monstre)

    def ajouter_tresor(self, tresor):
        self.tresors.append(tresor)

    def ajouter_boss(self, boss):
        self.boss.append(boss)

    def afficher_salles(self):
        print("Salles de", self.nom + ":")
        for salle in self.salles:
            print("-", salle)

    def afficher_monstres(self):
        print("\nMonstres dans", self.nom + ":")
        for monstre in self.monstres:
            print("-", monstre.nom)

    def afficher_tresors(self):
        print("\nTrésors dans", self.nom + ":")
        for tresor in self.tresors:
            print("-", tresor["Nom"], "(Valeur:", tresor["Valeur"], "pièces d'or)")

    def afficher_boss(self):
        print("\nBoss dans", self.nom + ":")
        for boss in self.boss:
            print("-", boss.nom)

    def afficher_geo_terrain(self):
        print("\nGéographie du terrain autour de", self.nom + ":", self.geo_terrain)

class Monstre:
    def __init__(self, nom, points_de_vie, attaque, defense):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.points_de_vie_restant = points_de_vie
        self.attaque = attaque
        self.defense = defense

class Boss:
    def __init__(self, nom, points_de_vie, attaque, defense):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.points_de_vie_restant = points_de_vie
        self.attaque = attaque
        self.defense = defense

class Arme:
    def __init__(self, nom, attaque, valeur):
        self.nom = nom
        self.attaque = attaque
        self.valeur = valeur

# Liste d'armes
armes_disponibles = [
    Arme("Épée en Fer", attaque=10, valeur=50),
    Arme("Arc Elfique", attaque=8, valeur=400),
    Arme("Hache de Guerre Naine", attaque=12, valeur=60),
    Arme("Dague Enchantée", attaque=10, valeur=300),
    Arme("Bâton de Sorcier", attaque=5, valeur=350)
]
# Liste de bosses
bosses = [
    Boss("Dracula, Seigneur des Vampires", points_de_vie=800, attaque=25, defense=20),
    Boss("Gorgoth, Roi des Gobelins", points_de_vie=600, attaque=22, defense=18),
    Boss("Nécros, Archiliche Squelette", points_de_vie=750, attaque=23, defense=15),
    Boss("Mortis, Maitre des Goules", points_de_vie=700, attaque=20, defense=22),
    Boss("Arak'Thar, Démon de l'Ombre", points_de_vie=900, attaque=28, defense=25)
]
# Liste de monstres
monstres = [
    Monstre("Gobelin", points_de_vie=30, attaque=8, defense=5),
    Monstre("Squelette", points_de_vie=40, attaque=10, defense=7),
    Monstre("Goule", points_de_vie=35, attaque=9, defense=6),
    Monstre("Harpie", points_de_vie=45, attaque=12, defense=8),
    Monstre("Loup-Garou", points_de_vie=50, attaque=15, defense=10),
    Monstre("Orc", points_de_vie=55, attaque=14, defense=9),
    Monstre("Banshee", points_de_vie=40, attaque=11, defense=7),
    Monstre("Ombre Sinueuse", points_de_vie=30, attaque=12, defense=6),
    Monstre("Chimère", points_de_vie=65, attaque=18, defense=12),
    Monstre("Basilic", points_de_vie=60, attaque=20, defense=15)
]


# Exemple d'utilisation
donjon_example = Donjon(
    "Donjon des Ténèbres",
    monstres=[Monstre("Gobelin", points_de_vie=30, attaque=8, defense=5)],
    tresors=[{"Nom": "Épée Enchantée", "Valeur": 300}],
    boss=[Boss("Seigneur Vampire", points_de_vie=800, attaque=25, defense=20)],
    geo_terrain="Forêt Sombre"
)

# Affichage du donjon créé
print("\nDonjon créé avec succès!")
donjon_example.ajouter_salle("Hall d'Entrée Sanglant")
donjon_example.ajouter_salle("Salle des Gobelins Piègeurs")
donjon_example.afficher_salles()
donjon_example.afficher_monstres()
donjon_example.afficher_tresors()
donjon_example.afficher_boss()
donjon_example.afficher_geo_terrain()