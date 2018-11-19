

import copy

###pièce=[x,y,forme,état]

def deplacement_droite(grille,piece):
    piece_copy=copy.deepcopy(grille)
    piece[0]+=1
    if position_possible(grille,piece):
        return piece
    else :
        return piece_copy


def deplacement_gauche(grille,piece):
    piece_copy=copy.deepcopy(grille)
    piece[0]-=1
    if position_possible(grille,piece):
        return piece
    else :
        return piece_copy

def deplacement_bas(grille,piece):
    piece_copy=copy.deepcopy(grille)
    piece[1]+=1
    if position_possible(grille,piece):
        return piece
    else :
        return piece_copy


def position_possible(grille,piece):
    coordones=coordonees(piece)



def coordonees(piece):
    t=###dictionnaire,piece[2],piec[3]
    y,x=piece[0],piece[1]
    coordones=[[y,x] for i in range(4)]
    for i in range(4):
        for j in range(2):
            coordones[i][j]+=t[i][j]
    return coordones


def rotation(grille,piece):
    piece_copy=copy.deepcopy(grille)
    piece[3]=(piece[3]+1)%4
    while superposition(piece,grille) :
        piece[1]-=1
    if position_possible(grille,piece):
        return piece
    else :
        return piece_copy
    
    
   
def superposition(piece,grille) :
    forme_piece=dico[piece[2]][piece[3]]
    forme=coordonees(forme_piece)
    for i in coordonees :
        if grille[piece[1]+i[0]][piece[0]+i[1]]!=0 :
            return True
    return False
