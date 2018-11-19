import numpy as np


def effacer_ligne(grille, i):
    grille_liste = grille.tolist()
    grille_liste = [grille_liste.pop(i)] + grille_liste
    return np.array(grille_liste)


def ligne_pleine(grille, i):
    grille_liste = grille.tolist()
    for k in range(len(grille_liste[i])):
        if grille_liste[i][k] == 0:
            return False
    return True

def detecte_ligne(grille):
    liste_lignes_pleines = []
    for i in range(len(grille)):
        if ligne_pleine(grille, i):
            liste_lignes_pleines.append(i)
    return liste_lignes_pleines
