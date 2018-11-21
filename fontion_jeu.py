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
    return int(max(0.2, 0.5 - niveau*0.5/7) * 1000)


#
def collision(piece,grille) :           ## Detecte si la piece entre en collision avec la grille
    Liste_piece=coordonees(piece)
    grille_copy=copy.deepcopy(grille)
    for i in Liste_piece :
        if i[0]==21 :
            for j in Liste_piece :
                grille_copy[j[0]][j[1]]+=piece[2]+1 ##On ajoute la clef de la piece
            return (True,grille_copy)
        else :
            if grille[i[0]+1][i[1]]!=0 :
                for k in Liste_piece :
                    grille_copy[k[0]][k[1]]+=piece[2]+1
                return (True,grille_copy)
    return (False,grille)           ##renvoie true ou false s'il y z collision avec la grille de jeu modifiee, et la nouvelle grille

