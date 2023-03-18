import string
import random
import colorama

# handle = open(r'C:\Users\Mohammed\Desktop\mot-mele\projet-python\mots.txt')
# liste_mots = handle.readline(4)

Level = input("Facile \t Moyen \t Difficile \n Tapez votre niveau de jeu :")


if (Level=="Facile"):
    Longueur = 10
    Hauteur = 5
if (Level=="Moyen"):
    Longueur = 15
    Hauteur = 7
if (Level=="Difficile"):
    Longueur = 30
    Hauteur = 15
if (Level!="Facile" and Level!="Moyen" and Level!="Difficile"): 
    print('Erreur de la selection de niveau ! , veuillez relancer votre jeu et réessayer')
    quit()
   
# Creation de la grille (liste) et danslaquelle on va generer des lettres en majuscule au hasard a l'interieur en fonction de la hauteur et largeur qu’on a choisie
# on parcour la hauteur et largeur grace au 'for in range' 
grille = [[random.choice(string.ascii_uppercase) for i in range(0,Longueur)] for j in range(0,Hauteur)]
 
#Fonction pour ajouter un mot dans la grille !
def ajout_mot(liste_mots,grille):
#On choisie aleatoirement de prendre le prendre le mot normalement ou de le prendre de maniere inverser 
    liste_mots = random.choice([liste_mots,liste_mots[::-1]]) 

# On met en place la direction qui sera choisie aleatoirement => en ligne ou en hauteur  (pas de diagonale)
    direction = random.choice([[1,0],[0,1]])

# verifions si la longueur du mot si elle rentre dans la grille ! verticalement ou horizontalement
# les 2 variables vont forcement rentrer dans la grille car leur valeur sera inferieur a la longueur de la grille sauf si le mot commence a l'extremité de la grille
 
    taille_x = Longueur if direction[0] == 0 else Longueur - len(liste_mots) 
    taille_y = Hauteur if direction[1] == 0 else Hauteur - len(liste_mots)
    global x,y
    x = random.randrange(0,taille_x)
    y = random.randrange(0,taille_y)
    
# Ajouton notre mot au hasard dans la grille

    for i in range(0,len(liste_mots)):
        
        grille[y+direction[1]*i][x+direction[0]*i] = liste_mots[i]
        
    return grille
#fin de la fonction
# initialisation de la liste de mot a trouver dans une liste 
reponse = []
if Level == 'Facile':
    liste_mots = ["WEB","PHP","SQL","BUG","BIT","IP"]
    for mot in liste_mots:
        grille = ajout_mot(mot,grille)
        reponse.append(mot)
        reponse.append(x)
        reponse.append(y)
        
if Level == 'Moyen':
    liste_mots = ["PATCHS","PYTHON","JAVA","ASCII"]
    for mot in liste_mots:
        grille = ajout_mot(mot,grille)
        reponse.append(mot)
        reponse.append(x)
        reponse.append(y)
if Level == 'Difficile':
    liste_mots = ["JAVASCRIPT","VULNERABILITE","CYBERATTAQUE","ALGORITHMIE"]
    for mot in liste_mots:
        grille = ajout_mot(mot,grille)
        reponse.append(mot)
        reponse.append(x)
        reponse.append(y)
#----------------------------------------------------------
print("\n".join(map(lambda row: "  ".join(row), grille)))
print("voici la liste de mot à trouver : ",liste_mots)
#-----------------------------------------------------------
    
mot = input ("le mot à chercher : ")
if mot  in liste_mots :
    print("True,ce mot",mot,"est bien dans la liste","cordonnee sont:",reponse)
else:
    print("False,ce mot",mot,"n'est pas dans la liste")


# cordonne_x = input("entrer la cordonnée X: ")
# cordonne_y = input("entrer la cordonnée y: ")









