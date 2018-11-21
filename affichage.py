from Tkinter import *
from deplacement_tetris import *
from grille_de_jeu import *
from pieces_etats import *

root = Tk()
root.title("Tetris")
top = Toplevel()

grille = cree_grille()
grille_graphique = [[[0] for _ in range(10)] for _ in range(22)]
for i in range(22):
    for j in range(10):
        case = Frame(top, row = i, column = j)
        grille_graphique[j][i] = case


root.mainloop()
top.mainloop()
