from pieces_etats import pieces_etat
import random as rd

#grille 22x10

def generer_piece(grille):
    num_aleatoire=rd.choice([0,1,2,3,4,5,6])
    piece_aleatoire= pieces_etat[num_aleatoire][0]
