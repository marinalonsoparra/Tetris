
import copy

from pieces_etats import*


# deplace la piece vers la droite sur la grille
#parametres: grille (list) (grille de 10*24,avec les piece deja jouees), piece: list (tableau de 4*4 ou 3*3 representant la piece)
#renvoie: piece (list): nouvelle liste codant l'etat et la disposition de la piece consideree
def deplacement_droite(grille,piece):
    piece_copy=copy.deepcopy(piece)
    piece_copy[1]+=1
    if  not depasse_droit(piece_copy) and not superposition(piece_copy,grille):
        return piece_copy
    else :
        return piece


# deplace la piece vers la gauche sur la grille
#parametres: grille (list) (grille de 10*24,avec les piece deja jouees), piece: list (tableau de 4*4 ou 3*3 representant la piece)
#renvoie: piece (list) (nouvelle liste codant l'etat et la disposition de la piece consideree)
def deplacement_gauche(grille,piece):
    piece_copy=copy.deepcopy(piece)
    piece_copy[1]-=1
    if  not depasse_gauche(piece_copy) and not superposition(piece_copy,grille):
        return piece_copy
    else :
        return piece



# deplace la piece vers le bas sur la grille
#parametres: grille (list) (grille de 10*24,avec les piece deja jouees), piece: list (tableau de 4*4 ou 3*3 representant la piece)
#renvoie: piece (list) (nouvelle liste codant l'etat et la disposition de la piece consideree)
def deplacement_bas(grille,piece):
    piece_copy=copy.deepcopy(piece)
    piece_copy[0]+=1
    if not superposition(piece_copy,grille):
        return piece_copy
    else:
        return piece


# donne les coordonnees des cubes de la piece
# parametres: piece (liste) (code la disposition de la piece et sa forme)
# renvoie coordones (liste) (liste des coordonnees sous forme de liste des carres de la piece)
def coordonees(piece):
    t=pieces_etat[piece[2]][piece[3]]
    y,x=piece[0],piece[1]
    coordones=[[y,x] for i in range(4)]
    for i in range(4):
        for j in range(2):
            coordones[i][j]+=t[i][j]
    return coordones


# donne la piece apres rotation de 90 degres
#parametres: grille (list) (grille de 10*24,avec les piece deja jouees), piece: list (tableau de 4 entiers representant la piece)
#renvoie: piece (list) (nouvelle liste codant l'etat et la disposition de la piece consideree),
# (si la piece depasse a gauche apres rotation, on la decale sur la droite pour la faire rentrer dans la grille)
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
#parametres: grille (list) (grille de 10*24,avec les piece deja jouees), piece: list (tableau de 4 entiers representant la piece)
#renvoie: True si la piece se superpose avec un element deja present dans la grille, ou si la piece sort de la grille par le bas, False sinon
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
#parametres: grille (list) (grille de 10*24,avec les piece deja jouees), piece: list (tableau de 4 entiers representant la piece)
#renvoie: True si la piece sort de la grille a droite, False sinon
def depasse_droit(piece):
    coordones=coordonees(piece)
    for i in coordones:
        if i[1]>9:
            return True
    return False


# teste si une piece depasse sur la gauche de la grille
#parametres: grille (list) (grille de 10*24,avec les piece deja jouees), piece: list (tableau de 4 entiers representant la piece)
#renvoie: True si la piece sort de la grille a gauche, False sinon
def depasse_gauche(piece):
    coordones=coordonees(piece)
    for i in coordones:
        if i[1]<0:
            return True
    return False

# fonction finale regroupant tous les deplacements
#parametres: grille (list) (grille de 10*24,avec les piece deja jouees), piece: list (tableau de 4 entiers representant la piece), deplacement: (str) defini le deplacement voulu
#renvoie: deplacement_droite(grille,piece) si le deplacement est demande a droite
#deplacement_gauche(grille,piece) si le deplacement est demande a gauche
#rotation(grille,piece) si le deplacement est demande est haut
#deplacement_bas(grille,piece) si le deplacement est demande en bas

def deplacement_piece(grille, piece,deplacement):
    if deplacement=='Right':
        return deplacement_droite(grille,piece)
    elif deplacement=='Left':
        return deplacement_gauche(grille,piece)
    elif deplacement=='Up':
        return rotation(grille,piece)
    elif deplacement=='Down':
        return deplacement_bas(grille,piece)
    else :
        return piece



