import numpy as np

import copy
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
print(pieces_etat[1])
###piece=[y,x,forme,etat]

def deplacement_droite(grille,piece):
    piece_copy=copy.deepcopy(piece)
    piece_copy[1]+=1
    if  not depasse_droit(piece) and not superposition(piece,grille):
        return piece_copy
    else :
        return piece


def deplacement_gauche(grille,piece):
    piece_copy=copy.deepcopy(piece)
    piece_copy[1]-=1
    if  not depasse_gauche(piece) and not superposition(piece,grille):
        return piece_copy
    else :
        return piece


def deplacement_bas(grille,piece):
    piece_copy=copy.deepcopy(grille)
    piece[0]+=1
    if position_possible(grille,piece):
        return piece
    else :
        return piece_copy


def coordonees(piece):
    t=pieces_etat[piece[2]][piece[3]]
    y,x=piece[0],piece[1]
    coordones=[[y,x] for i in range(4)]
    for i in range(4):
        for j in range(2):
            coordones[i][j]+=t[i][j]
    return coordones


def rotation(grille,piece):
    piece[3]=(piece[3]+1)%4
    while depasse_droit(piece) :
        piece[1]-=1
    while depasse_gauche(piece) :
        piece[1]+=1
    while superposition(piece,grille) :
            piece[0]-=1
    return piece


def superposition(piece,grille) :
    coord=coordonees(piece)
    for i in coord :
        if grille[i[0]][i[1]]!=0 :
            return True
    return False


def depasse_droit(piece):
    coordones=coordonees(piece)
    for i in coordones:
        if i[1]>9:
            return True
    return False


def depasse_gauche(piece):
    coordones=coordonees(piece)
    for i in coordones:
        if i[1]<0:
            return True
    return False    



