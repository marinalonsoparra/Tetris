import numpy as np
import copy
from pieces_etats import pieces_etat
import random as rd
from deplacement_tetris import *



def cree_grille() :
    return np.zeros((22,10)).tolist()

# efface la ligne i de la grille et crée une nouvelle ligne en haut de la grille
def effacer_ligne(grille, i):
    grille_bis = copy.deepcopy(grille)
    del grille_bis[i]
    grille_bis = [[0 for i in range(10)]] + grille_bis
    return grille_bis


# regarde si la ligne i de la grille est pleine
def ligne_pleine(grille, i):
    for k in range(len(grille[i])):
        if grille[i][k] == 0:
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
    grille_bis = copy.deepcopy(grille)
    for c in detecte_ligne(grille_bis):
        grille_bis = effacer_ligne(grille_bis, c)
    return grille_bis

#renvoie un nouvelle piece (y=0,etat=0, x et forme aleatoire)
def generer_piece():

    form=rd.choice([0,1,2,3,4,5,6])
    y=0
    x=rd.randint(0,9)
    piece=[y,x,form,0]
    while depasse_droit(piece):
        x=rd.randint(0,9)
        piece=[y,x,form,0]
    return piece
