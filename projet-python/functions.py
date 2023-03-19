import random
import string
from termcolor import colored
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

def verif_mot(mot, liste_mots):
    for i in liste_mots:
        if mot in i:
            return True
    return False

def verif_coord(mot,reponse,cordo_x,cordo_y,taille):
    for i in reponse:
        
        if mot==reponse[0] and cordo_x==reponse[1] and cordo_y==reponse[2] and taille=='3' or mot==reponse[3] and cordo_x==reponse[4] and cordo_y==reponse[5] and taille=='3' or mot==reponse[6] and cordo_x==reponse[7] and cordo_y==reponse[8] and taille=='3' or mot==reponse[9] and cordo_x==reponse[10] and cordo_y==reponse[11] and taille=='3' or mot==reponse[12] and cordo_x==reponse[13] and cordo_y==reponse[14] and taille=='3' or mot==reponse[15] and cordo_x==reponse[16] and cordo_y==reponse[17] and taille=='2':  
            return True
        else:
            return False
        
def colorize_element_in_list(lst, element, color):
    """Met en couleur un élément au sein d'une liste."""
    for i, item in enumerate(lst):
        if item == element:
            lst[i] = colored(item, color)
    return lst
        

