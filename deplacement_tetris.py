import numpy as np

import copy


# * * * *


# * * * *

etat_piece_0={0:[(1,0),(1,1),(1,2),(1,3)],\
              1:[(0,2),(1,2),(2,2),(3,2)],\
              2:[(2,0),(2,1),(2,2),(2,3)],\
              3:[(0,1),(1,1),(2,1),(3,1)]}


# *
# * * *
etat_piece_1={0:[(0,0),(1,0),(1,1),(1,2)],\
              1:[(0,1),(0,2),(1,1),(2,1)],\
              2:[(1,0),(1,1),(1,2),(2,2)],\
              3:[(0,1),(1,1),(2,1),(2,0)]}

#     *
# * * *
etat_piece_2={0:[(0,2),(1,0),(1,1),(1,2)],\
              1:[(0,1),(1,1),(2,1),(2,2)],\
              2:[(1,0),(1,1),(1,2),(2,0)],\
              3:[(0,0),(0,1),(1,1),(2,1)]}

# * *
# * *
etat_piece_3={0:[(0,1),(0,2),(1,1),(1,2)],\
              1:[(0,1),(0,2),(1,1),(1,2)],\
              2:[(0,1),(0,2),(1,1),(1,2)],\
              3:[(0,1),(0,2),(1,1),(1,2)]}

#   * *
# * *
etat_piece_4={0:[(0,1),(0,2),(1,0),(1,1)],\
              1:[(0,1),(1,1),(1,2),(2,2)],\
              2:[(1,1),(1,2),(2,0),(2,1)],\
              3:[(0,0),(1,0),(1,1),(2,1)]}

#   *
# * * *
etat_piece_5={0:[(0,1),(1,0),(1,1),(1,2)],\
              1:[(0,1),(1,1),(1,2),(2,1)],\
              2:[(1,0),(1,1),(1,2),(2,1)],\
              3:[(0,1),(1,0),(1,1),(2,1)]}

#   * *
#     * *
etat_piece_6={0:[(0,0),(0,1),(1,1),(1,2)],\
              1:[(0,2),(1,1),(1,2),(2,1)],\
              2:[(1,0),(1,1),(2,1),(2,2)],\
              3:[(0,1),(1,0),(1,1),(2,0)]}

pieces_etat={0:etat_piece_0,1:etat_piece_1,2:etat_piece_2,3:etat_piece_3,4:etat_piece_4,5:etat_piece_5,6:etat_piece_6}
###piece=[y,x,forme,etat]

# deplace la piece vers la droite sur la grille
def deplacement_droite(grille,piece):
    piece_copy=copy.deepcopy(piece)
    piece_copy[1]+=1
    if  not depasse_droit(piece_copy) and not superposition(piece_copy,grille):
        return piece_copy
    else :
        return piece


# deplace la piece vers la gauche sur la grille
def deplacement_gauche(grille,piece):
    piece_copy=copy.deepcopy(piece)
    piece_copy[1]-=1
    if  not depasse_gauche(piece_copy) and not superposition(piece_copy,grille):
        return piece_copy
    else :
        return piece



# deplace la piece vers le bas sur la grille
def deplacement_bas(grille,piece):
    piece_copy=copy.deepcopy(piece)
    piece_copy[0]+=1
    if not superposition(piece_copy,grille):
        return piece_copy
    else:
        return piece


# renvoie les coordonnees des cubes de la piece
def coordonees(piece):
    t=pieces_etat[piece[2]][piece[3]]
    y,x=piece[0],piece[1]
    coordones=[[y,x] for i in range(4)]
    for i in range(4):
        for j in range(2):
            coordones[i][j]+=t[i][j]
    return coordones


# renvoie la piece apres rotation de 90 degres
def rotation(grille,piece):
    piece[3]=(piece[3]+1)%4
    while depasse_droit(piece) :
        piece[1]-=1
    while depasse_gauche(piece) :
        piece[1]+=1
    while superposition(piece,grille) :
            piece[0]-=1
    return piece


# teste si la piece se superpose avec une piece de la grille
def superposition(piece,grille) :
    coord=coordonees(piece)
    for i in coord :
        try:
            if grille[i[0]][i[1]]!=0 :
                return True
        except IndexError:
            return True
    return False


# teste si une piece depasse sur la droite de la grille
def depasse_droit(piece):
    coordones=coordonees(piece)
    for i in coordones:
        if i[1]>9:
            return True
    return False


# teste si une piece depasse sur la gauche de la grille
def depasse_gauche(piece):
    coordones=coordonees(piece)
    for i in coordones:
        if i[1]<0:
            return True
    return False

# deplacement
def deplacement_piece(grille, piece,deplacement):
    if deplacement=='d':
        return deplacement_droite(grille,piece)
    elif deplacement=='g':
        return deplacement_gauche(grille,piece)
    elif deplacement=='h':
        return rotation(grille,piece)
    elif deplacement=='b':
        return deplacement_bas(grille,piece)
    else :
        return piece



