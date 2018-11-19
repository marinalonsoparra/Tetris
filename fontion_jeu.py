from time import*

def test_fin_jeu (grille) :
    res=grille.T
    for i in res :
        if 0 in i :
            return False
    return True


def horloge(n,difficulté) :
    sleep(max(0.2,1-difficulté/(difficulté+1+n)))
