from tkinter import *

frame= Tk()
title=Message(frame, text="Choose your level:", font=("Times", "24", "bold") )
set_niveau= Listbox(frame, height=7, fg='white',bg='grey', selectmode='SINGLE')
set_niveau.insert(1,"Level 0")
set_niveau.insert(2,"Level 1")
set_niveau.insert(3,"Level 3")
set_niveau.insert(4,"Level 4")
set_niveau.insert(5,"Level 5")
set_niveau.insert(6,"Level 6")
set_niveau.insert(7,"Maximum Level")
title.pack()
set_niveau.pack()


frame.mainloop()

