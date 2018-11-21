#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deplacement_tetris.py import *
from time import*
import numpy as np

def test_fin_jeu (grille) :
res=np.array(grille).T
for i in res :
if len(i)>22 :
return True
return False


def horloge(n, difficulte) :
sleep(max(0.2, 1 - difficulte / (difficulte + 1 + n)))

def collision(piece,grille) :
Liste_piece=coordonees(piece)
grille_copy=copy.deepcopy(grille)
for i in Liste_piece :
if i[0]==22 :
for j in liste_piece :
    grille[j[0]][j[1]]+=pieces_etat.keys()[pieces_etat.values().index(piece)]
else :
if grille[i[0]][i[1]+1]!=0 :
    for k in liste_piece :
        grille_copy[k[0]][k[1]]+=pieces_etat.keys()[pieces_etat.values().index(piece)]
    return (True,grille_copy)
return (False,grille)
