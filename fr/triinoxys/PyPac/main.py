from tkinter import * #@UnusedWildImport
from tkinter.messagebox import askyesno #@UnusedWildImport @Reimport
 
def quit():  #@ReservedAssignment
    if askyesno('Quitter', 'Êtes-vous sur de vouloir quitter ?'):
        fen1.destroy()
 
def keypress(event):
    global can1
    if event.keysym == "Left":  can1.move("pacman",-5,  0)
    if event.keysym == "Right": can1.move("pacman", 5,  0)
    if event.keysym == "Up":    can1.move("pacman", 0, -5)
    if event.keysym == "Down":  can1.move("pacman", 0,  5)
    
 
fen1 = Tk()
fen1.title("PyPac")
   
photo1 = PhotoImage(file="sprites/objs/bg.png")
photo2 = PhotoImage(file="sprites/pacman/closed.png")
   
can1 = Canvas(fen1, width=500, height=546)
can1.create_image(0, 0, anchor=NW, image=photo1, tags="bg")
can1.create_image(249, 210, image=photo2, tags="pacman")
can1.pack()
   
bou1 = Button(fen1, text='Quitter', command=quit)
bou1.pack()
   
fen1.bind_all('<Key>', keypress)
   
fen1.mainloop()