from threading import Thread
from son import*
from tkinter import*
import pygame
from deplacement_tetris import *
from grille_de_jeu import *
from pieces_etats import *
from grille_de_jeu import *
from pieces_etats import *
from fontion_jeu import *
import time

class music(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):                  ##Si la musique se termine, la relance
            while True :                   ##Si la musique se termine, la relance
                try:
                    initMixer()             ##Lance la musique
                    pmusic(file)
                except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
                    stopmusic()
                    print("\nPlay Stopped by user")
                    break


class display(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):

        root = Tk()
        root.title("Tetris")
        top = Toplevel()

        global niveau
        niveau = 1

        global grille
        grille = cree_grille()
        global grille_graphique
        grille_graphique = [[0 for _ in range(10)] for _ in range(22)]

        for i in range(22):
                for j in range(10):
                    case = Frame(top, bg = 'black', relief = 'groove', bd = 0.5, width = 30, height = 30)
                    case.grid(row = i, column = j)
                    grille_graphique[i][j] = case

        global piece
        piece = generer_piece()

        ##Fonctions
        def mise_a_jour_grille_graph():
                global piece
                global grille_graphique
                global grille

                grille_provisoire = copy.deepcopy(grille)
                forme = piece[2]
                for c in coordonees(piece):
                    grille_provisoire[c[0]][c[1]] = forme + 1
                for i in range(22):
                    for j in range(10):
                        grille_graphique[i][j].config(bg = piece_coleur[grille_provisoire[i][j]])

        def KeyPressed(event):
            global piece
            global grille_graphique
            d = event.keysym
            piece = deplacement_piece(grille, piece, d)
            mise_a_jour_grille_graph()


        def start_game():
            global grille
            global piece
            global niveau

            piece=deplacement_piece(grille,piece,'Down')
            mise_a_jour_grille_graph()
            if collision(piece, grille)[0]:
                grille = collision(piece,grille)[1]
                piece = generer_piece()
            top.after(1000, start_game)



        start = Button(root, text = 'Start Game', command = start_game)
        start.grid()
        top.bind('<Key>', KeyPressed)
        root.mainloop()
        top.mainloop()




thA=display()
thM=music()

thA.start()
thM.start()

thA.join()
thM.join()





