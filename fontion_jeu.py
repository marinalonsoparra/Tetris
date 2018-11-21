#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deplacement_tetris import *
from time import *
from grille_de_jeu import *

from deplacement_tetris import*
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
        if i[0]==21 :
            for j in Liste_piece :
                grille[j[0]][j[1]]+=pieces_etat.keys()[pieces_etat.values().index(piece)]+1
                return (True,grille)##On ajoute la clef de la piece
        else :
            if grille[i[0]][i[1]+1]!=0 :
                for k in Liste_piece :
                    grille_copy[k[0]][k[1]]+=pieces_etat.keys()[pieces_etat.values().index(piece)]
                return (True,grille_copy)
    return (False,grille)           ##renvoie true ou false s'il y z collision avec la grille de jeu modifiee, et la nouvelle grille

