#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import*
import numpy as np

def test_fin_jeu (grille) :
    res=np.array(grille).T
    for i in res :
        if 0 in i :
            return False
    return True


def horloge(n, difficulte) :
    sleep(max(0.2, 1 - difficulte / (difficulte + 1 + n)))

