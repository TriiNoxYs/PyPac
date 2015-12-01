from tkinter import *
from tkinter.messagebox import *

def quit():
    if askyesno('Quitter', 'Êtes-vous sûr de vouloir quitter ?'):
        fen1.destroy()


fen1 = Tk()
fen1.title("PyPac")


bou1 = Button(fen1, text='Quitter', command=quit)
bou1.pack()

photo1 = PhotoImage(file="bg.png")
can1 = Canvas(fen1, width=500, height=546)
can1.create_image(0, 0, anchor=NW, image=photo1)
can1.pack()

fen1.mainloop()