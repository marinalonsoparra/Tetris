from tkinter import *

def frame_scores(left_frame, score, level, line, font_tetrix):

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

    label_level_num = Label(left_frame, text=str(level), fg="white", background=number_background_color,width=width_num, height=height_num)
    label_level_num.grid(row=3,column=0)


    label_line = Label(left_frame, text="LINES", fg="white", font=font_tetrix, background=frame_background_color,width=width_num+3, height=height_num)
    label_line.grid(row=4,column=0)

    label_line_num = Label(left_frame, text=str(line), fg="white", background=number_background_color,width=width_num, height=height_num)
    label_line_num.grid(row=5,column=0)

    label_vide = Label(left_frame, text="", background=frame_background_color)
    label_vide.grid(row=6,column=0)
