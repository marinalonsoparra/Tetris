from tkinter import *

from grille_de_jeu import *
from pieces_etats import *



def frame_pieces(right_frame,piece, font_tetrix):
    width_num=10
    height_num=30
    number_background_color="#424949"
    frame_background_color="grey"

    right_frame.config(background=frame_background_color, relief ='groove', highlightthickness=1)

    label_score = Label(right_frame, text="NEXT", fg="white", font=font_tetrix, background="grey")
    label_score.grid(row=0,column=0)

    label_grid = Label(right_frame, background=number_background_color, relief ='groove', highlightthickness=1, width=width_num, height=height_num)
    label_grid.grid(row=1,column=0)

    grille_graphique = [[0 for _ in range(4)] for _ in range(4)]
    grille_provisoire = [[0 for _ in range(4)] for _ in range(4)]

    forme=piece[2]

    for i in range(4):
        for j in range(4):
            case = Frame(label_grid, bg = number_background_color, width = 30, height = 30)
            case.grid(row = i, column = j)
            grille_graphique[i][j] = case

    for c in coordonees(piece):
             grille_provisoire[c[0]][c[1]-3] = forme+1
             for i in range(4):
                for j in range(4):
                    if grille_provisoire[i][j]!=0:
                        grille_graphique[i][j].config(bg = piece_coleur[grille_provisoire[i][j]],relief = 'groove',bd = 0.5)







