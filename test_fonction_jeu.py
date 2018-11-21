from Tetrix.fontion_jeu import *
from Tetrix.deplacement_tetris import *

def test_collision():
    grille=[[0 for i in range (0,10)] for j in range (0,22)]
    piece=[19,0,1,3]
    assert collision(piece,grille)[0]==True
    for j in coordonees(piece):
                grille[j[0]][j[1]]+=piece[2]+1
    assert collision(piece,grille)[1]==grille
    piece_2=[2,5,1,3]
    assert collision(piece_2,grille)[0]==False
