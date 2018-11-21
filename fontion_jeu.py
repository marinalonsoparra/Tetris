#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deplacement_tetris.py import *
from time import *
from grille_de_jeu impo

# teste si le joueur a perdu
# parametres: grille (liste) (defini l'etat de la grille de jeu avec les differents blocs)
# renvoie: True sur la premiere et la deuxieme ligne sont non vides (lignes d'apparitions des pieces, toujours vides, sauf si ladite piece ne peut pas descendre)
def test_fin_jeu (grille) :
    if not (grille[0] == [0 for i in range(10)] and grille[1] == [0 for i in range(10)]):
        return True
    return False


def horloge(niveau) :
    sleep(max(0.2, 5 / (5 + niveau)))


#
def collision(piece,grille) :           ## Detecte si la piece entre en collision avec la grille
    Liste_piece=coordonees(piece)
    grille_copy=copy.deepcopy(grille)
    for i in Liste_piece :
        if i[0]==22 :
            for j in liste_piece :
                grille[j[0]][j[1]]+=pieces_etat.keys()[pieces_etat.values().index(piece)]       ##ajoute la clef de la piece
        else :
            if grille[i[0]][i[1]+1]!=0 :
                for k in liste_piece :
                    grille_copy[k[0]][k[1]]+=pieces_etat.keys()[pieces_etat.values().index(piece)]
                return (True,grille_copy)
    return (False,grille)           ##renvoie true ou false s'il y z collision avec la grille de jeu modifiee, et la nouvelle grille

