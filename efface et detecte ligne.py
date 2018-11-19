# efface la ligne i de la grille et crée une nouvelle ligne en haut de la grille
def effacer_ligne(grille, i):
    grille_bis = copy.deepcopy(grille)
    del grille_bis[i]
    grille_bis = [[0 for i in range(10)]] + grille_bis
    return grille_bis



# regarde si la ligne i de la grille est pleine
def ligne_pleine(grille, i):
    for k in range(len(grille[i])):
        if grille[i][k] == 0:
            return False
    return True


# renvoie la liste des lignes pleines de la grille
def detecte_ligne(grille):
    liste_lignes_pleines = []
    for i in range(len(grille)):
        if ligne_pleine(grille, i):
            liste_lignes_pleines.append(i)
    return liste_lignes_pleines


# renvoie la grille après avoir supprimé les lignes pleines
def traitement_grille(grille, score, niveau):
    grille_bis = copy.deepcopy(grille)
    liste_lignes_pleines = detecte_ligne(grille_bis)
    for c in liste_lignes_pleines:
        grille_bis = effacer_ligne(grille_bis, c)
    if len(liste_lignes_pleines) == 1:
        score += 40*(niveau + 1)
        elif len(liste_lignes_pleines) == 2:
            score += 100*(niveau + 1)
            elif len(liste_lignes_pleines) == 3:
                score += 300*(niveau + 1)
                elif len(liste_lignes_pleines) == 4:
                    score += 1200*(niveau + 1)
    return grille_bis
