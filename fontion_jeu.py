def test_fin_jeu (grille) :
    res=grille.T
    for i in res :
        if 0 in i :
            return False
    return True
