import random
import string

def choix_lvl(Level):
    
    global Longueur
    global Hauteur
    
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
        
Level = input("Facile \t Moyen \t Difficile \n Tapez votre niveau de jeu :")
choix_lvl(Level)
   
# Creation de la grille (liste) et danslaquelle on va generer des lettres en majuscule au hasard a l'interieur en fonction de la hauteur et largeur qu’on a choisie
# on parcour la hauteur et largeur grace au 'for in range' 
grille = [[random.choice(string.ascii_uppercase) for i in range(0,Longueur)] for j in range(0,Hauteur)]

def verif_mot(mot,reponse,cordo_x,cordo_y,taille): 
    print(reponse)   
    
    for i in reponse:
        print(i)