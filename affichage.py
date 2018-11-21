from tkinter import *
from grille_de_jeu import *
from pieces_etats import *
from fontion_jeu import *
import time
import pygame
from threading import Thread
from son import*

class music(Thread):
    def __init__(self,theme):
        Thread.__init__(self)
        self.theme=theme
    def run(self):                  ##Si la musique se termine, la relance
            while True :                   ##Si la musique se termine, la relance
                try:
                    initMixer()             ##Lance la musique
                    pygame.init()
                    pygame.mixer.init()
                    clock = pygame.time.Clock()
                    pygame.mixer.music.load(self.theme)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():

                        clock.tick(1000)
                except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
                    stopmusic()
                    print("\nPlay Stopped by user")
                    break


def affichage_grille():

    global score
    global nombre_lignes_supprimees
    score = 0
    nombre_lignes_supprimees = 0
    root = Tk()
    root.title("Tetris")
    top = Toplevel()
    labeltaille = Label(root, text = 'niveau')
    labeltaille.grid(row = 0)

    f1 = Frame(root)
    spinbox = Spinbox(f1, from_ = 1, to = 15)
    f1.grid(row = 1)
    spinbox.grid()

    f2 = Frame(root)

    listbox = Listbox(f2, height = 4, selectmode = 'single')
    listbox.insert(0, r'Default.mp3')
    listbox.insert(1, r'Dubstep.mp3')
    listbox.insert(2, r'Acoustic.mp3')
    listbox.insert(3, r'Trap.mp3')
    f2.grid(row = 3)
    listbox.grid()
    global niveau
    niveau = int(spinbox.get())

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

    #Fenetre score
    left_frame = Toplevel()
    font_tetrix = 'Helvetica'
    width_num=10
    height_num=1
    number_background_color="#424949"
    frame_background_color="grey"

    left_frame.config(background=frame_background_color, highlightthickness=1,)

    label_score = Label(left_frame, text="SCORE", fg="white", font=font_tetrix, background="grey",width=width_num+3, height=height_num)
    label_score.grid(row=0,column=0)

    label_score_num = Label(left_frame, text=str(score), fg="white", background=number_background_color,width=width_num, height=height_num)
    label_score_num.grid(row=1,column=0)


    label_level = Label(left_frame, text="LEVEL", fg="white", font=font_tetrix, background=frame_background_color,width=width_num+3, height=height_num)
    label_level.grid(row=2,column=0)

    label_level_num = Label(left_frame, text=str(niveau), fg="white", background=number_background_color,width=width_num, height=height_num)
    label_level_num.grid(row=3,column=0)


    label_line = Label(left_frame, text="LINES", fg="white", font=font_tetrix, background=frame_background_color,width=width_num+3, height=height_num)
    label_line.grid(row=4,column=0)

    label_line_num = Label(left_frame, text=str(nombre_lignes_supprimees), fg="white", background=number_background_color,width=width_num, height=height_num)
    label_line_num.grid(row=5,column=0)

    label_vide = Label(left_frame, text="", background=frame_background_color)
    label_vide.grid(row=6,column=0)

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
        global nombre_lignes_supprimees
        global score
        if not test_fin_jeu(grille):
            mise_a_jour_grille_graph()
            piece=deplacement_piece(grille,piece,'Down')
            mise_a_jour_grille_graph()
            if collision(piece, grille)[0]:
                grille = collision(piece, grille)[1]
                traitement = traitement_grille(grille, score, nombre_lignes_supprimees)
                grille = traitement[0]
                score = traitement[1]
                nombre_lignes_supprimees = traitement[2]
                piece = generer_piece()
                mise_a_jour_grille_graph()
                label_line_num.config(text = str(nombre_lignes_supprimees))
                label_score_num.config(text = str(score))
                label_level_num.config(text = str(niveau))
            niveau = nombre_lignes_supprimees // 10
        theme=listbox.curselection()
        print(theme)
        thM=music(theme)
        thM.start()
        thM.join()
        piece=deplacement_piece(grille,piece,'Down')
        mise_a_jour_grille_graph()
        if collision(piece, grille)[0]:
            grille = collision(piece, grille)[1]
            traitement = traitement_grille(grille, score, nombre_lignes_supprimees)
            grille = traitement[0]
            score = traitement[1]
            nombre_lignes_supprimees = traitement[2]
            piece = generer_piece()
            mise_a_jour_grille_graph()
        niveau = nombre_lignes_supprimees // 10

            top.after(horloge(niveau), start_game)
        else:
            print('game over')


    start = Button(root, text = 'Start Game', command = start_game)
    start.grid()
    top.bind('<Key>', KeyPressed)
    root.mainloop()
    top.mainloop()
    left_frame.mainloop()



affichage_grille()
