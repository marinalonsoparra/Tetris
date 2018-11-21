import numpy as np
import copy
from pieces_etats import pieces_etat

import random as rd
from deplacement_tetris import *

# cree la grille de jeu
# parametres: None
# renvoie: grille (list) une grille de 0 de dimension 10*22
def cree_grille() :
    return np.zeros((22,10)).tolist()

# efface la ligne i de la grille et crée une nouvelle ligne en haut de la grille
# parametres: grille (list) (grille de jeu,10*22)
# i (int) (rang de la ligne a detruire)
# renvoie: grille (list) (nouvelle grille de jeu)

def effacer_ligne(grille, i):
    grille_bis = copy.deepcopy(grille)
    del grille_bis[i]
    grille_bis = [[0 for i in range(10)]] + grille_bis
    return grille_bis


# regarde si la ligne i de la grille est pleine (d'entiers differents de 0)
# parametres: grille (list) (grille de jeu,10*22)
# i (int) (rang de la ligne a traiter)
# renvoie True si la ligne est pleine, False sinon
def ligne_pleine(grille, i):
    for k in range(len(grille[i])):
        if grille[i][k] == 0:
            return False
    return True


# renvoie la liste des lignes pleines de la grille
# parametres: grille (list) (grille de jeu,10*22)
# renvoie liste_ligne_pleines (list) (liste des rangs des lignes de la grille de jeu pleine d'entiers differents de 0)
def detecte_ligne(grille):
    liste_lignes_pleines = []
    for i in range(len(grille)):
        if ligne_pleine(grille, i):
            liste_lignes_pleines.append(i)
    return liste_lignes_pleines


# renvoie la grille après avoir supprimé les lignes pleines, update le score en fonction du nombre de lignes supprimees et le nombre totale de lignes supprimees
# parametres: grille (list) (grille de jeu,10*22)
# score (int) (score du joueur)
# nombre_ligne_supprimees (int) (nombre de ligne supprimees par le joueur au cours de la partie)
# renvoie grille (list) (grille traitee)

def traitement_grille(grille, score, nombre_lignes_supprimees):
    niveau = nombre_lignes_supprimees // 10
    grille_bis = copy.deepcopy(grille)
    liste_lignes_pleines = detecte_ligne(grille_bis)
    nombre_lignes_pleines = len(liste_lignes_pleines)
    for c in liste_lignes_pleines:
        grille_bis = effacer_ligne(grille_bis, c)
    if nombre_lignes_pleines == 1:
        score += 40*(niveau + 1)
    else:
        if nombre_lignes_pleines == 2:
            score += 100*(niveau + 1)
        else:
            if nombre_lignes_pleines == 3:
                score += 300*(niveau + 1)
            else:
                if nombre_lignes_pleines == 4:
                    score += 1200*(niveau + 1)
    nombre_lignes_supprimees += nombre_lignes_pleines
    return(grille_bis)


#renvoie un nouvelle piece (y=0,etat=0, x et forme aleatoire)
# parametres: None
# renvoie: piece (list) (liste codant une piece de forme aleatoire dans la position 0, cf le dictionnaire des pieces de deplacement_tetris)
def generer_piece():
    form=rd.choice([0,1,2,3,4,5,6])
    y=0
    x=3
    piece=[y,x,form,0]
    return piece
