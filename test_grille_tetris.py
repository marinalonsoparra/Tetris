import pytest
import numpy as np
from grille_de_jeu import *


def test_create_grid():
    assert create_grid()== np.array([[0 for i in range (0,10)] for j in range (0,22)])

def test_detecte_ligne():
    grid=[[1  for i in range (0,10)] for j in range (0,22)]
    assert detecte_ligne(grid,4)==True
    grid_2=[[0  for i in range (0,10)] for j in range (0,22)]
    assert detecte_ligne(grid,5)==False


def test_effacer_ligne():
    grid=np.array([[0 for i in range (0,10)] for j in range (0,22)])
    grid[0,1]=1
    grid[1,0]=2
    test_grid=np.array([[0 for i in range (0,10)] for j in range (0,22)])
    assert effacer_ligne(grid,0)== test_grid
    test_grid[2,0]=2
    test_grid[1,1]=1
    assert effacer_ligne(grid,10)== test_grid


def test_generate_piece():

def 




