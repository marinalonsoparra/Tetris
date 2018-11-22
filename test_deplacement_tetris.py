from deplacement_tetris import *


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

def test_deplacement_bas():
    grille=[[0 for i in range (0,10)] for j in range (0,22)]
    piece=[0,0,1,3]
    assert deplacement_bas(grille,piece) == [1,0,1,3]
    piece_2=[19,3,2,3]
    assert deplacement_bas(grille,piece_2) == [19,3,2,3]

def test_coordonnees_piece():
    piece=[0,0,1,3]
    assert coordonees(piece)==[[0,1],[1,1],[2,1],[2,0]]
    piece_2=[2,2,1,3]
    assert coordonees(piece_2)==[[2,3],[3,3],[4,3],[4,2]]

def test_rotation():
    piece=[4,7,1,3]
    grille=[[0 for i in range (0,10)] for j in range (0,22)]
    assert rotation(grille,piece)==[4,7,1,0]
    piece_2=[4,8,0,3]
    assert rotation(grille,piece_2)==[4,6,0,0]

def test_superposition():
    piece_2=[4,6,1,3]
    grille=[[0 for i in range (0,10)] for j in range (0,22)]
    piece=[19,0,1,3]
    assert superposition(piece,grille)== False
    assert superposition(piece_2, grille)== False

def test_depasse():
    piece_2=[4,9,1,3]
    grille=[[0 for i in range (0,10)] for j in range (0,22)]
    assert depasse_droit(piece_2)==True
    assert depasse_gauche(piece_2)==False

def test_deplacement_piece():
    grille=[[0 for i in range (0,10)] for j in range (0,22)]
    piece=[4,9,1,3]
    assert deplacement_piece(grille,piece,'d')==deplacement_droite(grille,piece)
    assert deplacement_piece(grille,piece,'g')==deplacement_gauche(grille,piece)
    assert deplacement_piece(grille,piece,'h')==rotation(grille,piece)
    assert deplacement_piece(grille,piece,'b')==deplacement_bas(grille,piece)






