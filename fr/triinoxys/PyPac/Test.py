import sys, os
from tkinter import *
from _ast import operator
from _operator import itemgetter
from asyncore import loop
p = itemgetter
fenetre = Tk()
loop;
print("Debug")
fenetre.mainloop()
photo = PhotoImage(file="PyPac/sprites/dying/0.png")
canvas = Canvas(fenetre,width=450, height=400)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
