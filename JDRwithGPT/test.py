# Liste des salles de donjon
salles_donjon = [
    "Hall d'Entrée Sanglant",
    "Salle des Gobelins Piègeurs",
    "Crypte des Squelettes Agiles",
    "Salon des Vampires Affamés",
    "Chambre des Miroirs Trompeurs",
    "Salle des Goules Rampantes",
    "Cachots des Victimes en Sommeil",
    "Forge des Gobelins Artificiers",
    "Chambre du Trésor Maudit",
    "Salle du Rituel Sombre"
]

# Liste de trésors
tresors = [
    {"Nom": "Couronne en Ornement de Vampire", "Valeur": 500},
    {"Nom": "Épée Enchantée des Gobelins", "Valeur": 300},
    {"Nom": "Cape Sombrale de la Nuit Éternelle", "Valeur": 800},
    {"Nom": "Amulette de Résistance aux Miroirs", "Valeur": 400},
    {"Nom": "Dague d'Os des Squelettes", "Valeur": 250},
    {"Nom": "Potion de Sang de Goule", "Valeur": 150},
    {"Nom": "Collier de Perles de Vampire", "Valeur": 700},
    {"Nom": "Bourse d'Or Volée aux Gobelins", "Valeur": 350},
    {"Nom": "Statuette en Os de Squelette", "Valeur": 200},
    {"Nom": "Livre de Sorts Interdit des Vampires", "Valeur": 600},
    {"Nom": "Dague Emprisonnée des Goules", "Valeur": 300},
    {"Nom": "Cristal Sombre des Ténèbres", "Valeur": 450},
    {"Nom": "Bracelet Éthéré de la Crypte", "Valeur": 500},
    {"Nom": "Sceau Royal de Vampire", "Valeur": 700},
    {"Nom": "Écusson Gobelin de Défense", "Valeur": 250},
    {"Nom": "Lanterne d'Âme des Squelettes", "Valeur": 350},
    {"Nom": "Bague de Charme de Vampire", "Valeur": 600},
    {"Nom": "Écharpe Tissée de l'Ombre Goule", "Valeur": 200},
    {"Nom": "Talisman de Forge Gobelin", "Valeur": 400},
    {"Nom": "Coffre du Trésor Scellé", "Valeur": 1000},
    {"Nom": "Cape de Rituel des Vampires", "Valeur": 800},
    {"Nom": "Épée Spectrale des Goules", "Valeur": 450},
    {"Nom": "Fiole de Sang Magique de Vampire", "Valeur": 300},
    {"Nom": "Masque d'Illusion des Gobelins", "Valeur": 500},
    {"Nom": "Anneau de Résurrection Squelettique", "Valeur": 350},
    {"Nom": "Tablette Antique des Ténèbres", "Valeur": 600},
    {"Nom": "Pendentif d'Os de Goule", "Valeur": 250},
    {"Nom": "Perles de Sorcellerie de Vampire", "Valeur": 700},
    {"Nom": "Arbalète Gobeline Enchantée", "Valeur": 400},
    {"Nom": "Cristal des Ombres Squelettiques", "Valeur": 550}
]

# Affichage des salles de donjon
print("Salles de Donjon:")
for salle in salles_donjon:
    print("-", salle)

# Affichage des trésors
print("\nTrésors:")
for tresor in tresors:
    print("-", tresor["Nom"], "(Valeur:", tresor["Valeur"], "pièces d'or)")