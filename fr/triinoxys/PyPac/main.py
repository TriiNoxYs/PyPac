from tkinter import *
from tkinter.messagebox import askyesno

left_count = 0
right_count = 0
up_count = 0
down_count = 0
step = 5

def quit():
    if askyesno('Quitter', 'Êtes-vous sûr de vouloir quitter ?'):                        #Msgbox "Voulez-vous quitter ?" 
        fen1.destroy()                                                                   #Fermer l'app

def keypress(event):                                                                     #Event quand on presse une touche
    global left_count, right_count, up_count, down_count, step                           #Utilser les variables définies au dessus
    if(event.keysym == "Left"): left_count+=step                                         #Detecter la touche préssée 
    if(event.keysym == "Right"): right_count+=step
    if(event.keysym == "Up"): up_count+=step
    if(event.keysym == "Down"): down_count+=step
    can1.create_image(249-left_count+right_count, 210+down_count-up_count, image=photo2) #Déplacer le pacman
            

fen1 = Tk()                                                                              #Créer la fenetre
fen1.title("PyPac")                                                                      #Choisir le titre

photo1 = PhotoImage(file="sprites/objs/bg.png")                                          #Déclaration du background
photo2 = PhotoImage(file="sprites/pacman/closed.png")                                    #Déclaration du background

can1 = Canvas(fen1, width=500, height=546)                                               #Création du canevas (zone de dessins/images/objets/etc)
can1.create_image(0, 0, anchor=NW, image=photo1)                                         #Création du background
can1.create_image(249, 210, image=photo2)                                                #Premier pacman
can1.pack()

bou1 = Button(fen1, text='Quitter', command=quit)                                        #Boutton quitter
bou1.pack()

fen1.bind_all('<Key>', keypress)                                                         #Application de l'event keypress

fen1.mainloop()