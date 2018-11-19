from Tetrix.deplacement_tetris import *


def test_deplacement_droite():
    grille=[[0 for i in range (0,10)] for j in range (0,22)]
    piece=[0,0,1,3]
    assert deplacement_droite(grille,piece) == [0,1,1,3]
    piece_2=[0,9,2,3]
    assert deplacement_droite(grille,piece_2) == [0,9,2,3]

def test_deplacement_gauche():
    grille=[[0 for i in range (0,10)] for j in range (0,22)]
    piece=[0,0,1,3]
    assert deplacement_gauche(grille,piece) == piece
    piece_2=[0,9,2,3]
    assert deplacement_gauche(grille,piece_2) ==[0,8,2,3]
