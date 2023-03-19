import string
import random
import colorama
from functions import*
# handle = open(r'C:\Users\Mohammed\Desktop\mot-mele\projet-python\mots.txt')
# liste_mots = handle.readline(4)

 
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
        #parcour de la liste 
    for mot in liste_mots:
        #Appel de la fonction ajout_mot pour rajouter les mots 1 par 1
        grille = ajout_mot(mot,grille)
        #ajout les solutions dans une autre liste qu'on a precedemment appelle : reponse[]
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
mot=input("Rentrez le mot que vous avez trouvé: ")
cordo_x=input("Rentrez la cordonnée x (horizontale): ")
cordo_y=input("Rentrez la cordonnée y (verticale): ")
taille=input("Rentrez la taille du mot: ")
verif_mot(mot,reponse,cordo_x,cordo_y,taille)










