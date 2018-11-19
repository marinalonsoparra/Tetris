import pytest
import numpy as np
from grille_de_jeu import *


def test_creer_grille():
    assert creer_grille()== np.array([[0 for i in range (0,10)] for j in range (0,22)])

def test_detecte_ligne():
    grille=[[1  for i in range (0,10)] for j in range (0,22)]
    assert detecte_ligne(grille)==[i for i in range(0,22)]
    grille_2=[[0  for i in range (0,10)] for j in range (0,22)]
    assert detecte_ligne(grille)==[]


def test_effacer_ligne():
    grille=np.array([[0 for i in range (0,10)] for j in range (0,22)])
    grille[0,1]=1
    grille[1,0]=2
    test_grid=np.array([[0 for i in range (0,10)] for j in range (0,22)])
    assert effacer_ligne(grille,0)== test_grid
    test_grid[2,0]=2
    test_grid[1,1]=1
    assert effacer_ligne(grille,10)== test_grid


def test_generate_piece():

def test_ligne_pleine():
    grille=[[1  for i in range (0,10)] for j in range (0,22)]
    assert ligne_pleine(grille,5)== True
    grille_2=[[0  for i in range (0,10)] for j in range (0,22)]
    assert detecte_ligne(grille, 4)==False





