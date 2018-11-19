import numpy as np


# efface la ligne i de la grille et crée une nouvelle ligne en haut de la grille
def effacer_ligne(grille, i): 
    a = grille.pop(i)
    grille = [[0 for i in range(grille(0))]] + grille
    return grille


# regarde si la ligne i de la grille est pleine
def ligne_pleine(grille, i):
    for k in range(len(grille[i])):
        if grille_liste[i][k] == 0:
            return False
    return True


# renvoie la liste des lignes pleines de la grille
def detecte_ligne(grille):
    liste_lignes_pleines = []
    for i in range(len(grille)):
        if ligne_pleine(grille, i):
            liste_lignes_pleines.append(i)
    return liste_lignes_pleines


# renvoie la grille après avoir supprimé les lignes pleines
def traitement_grille(grille):
    for c in detecte_ligne(grille):
        grille = effacer_ligne(grille, c)
