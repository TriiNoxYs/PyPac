#!/usr/bin/python

#--------------------------------------------------#
#
#Background  = 400 x 500 (var mapWidth et mapHeight)
#Le pacman se deplace de 5px en 5px (var step)
#Spawn = 201 342 (var x et y au depart)
#Les cases sont representÃ©es par la matrice                                                                                                                                  
#
#--------------------------------------------------#

import threading
import time
from tkinter import *   # @UnusedWildImport
from tkinter.messagebox import askyesno

direction = "None"
state = 1
step = 13
x = 204
y = 340                                                          

mapWidth  = 400
mapHeight = 500
blocked = False

loc = [23, 14]
matrix=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0], 
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0], 
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0], 
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
 


def quit():  #@ReservedAssignment
    if askyesno('Quitter', 'Êtes-vous sûr de vouloir quitter ?'):
        fen1.destroy()
        
 
def keypress(event):
    global can1, direction, matrix, state, x, y
    if event.keysym == "Left":
        direction = "Left"
        
    elif event.keysym == "Right":
        direction = "Right"
        
    elif event.keysym == "Up":
        direction = "Up"
        
    elif event.keysym == "Down":
        direction = "Down"
    
    elif event.keysym == "Escape":
        quit()
    
    while True:
        if direction == "None":
            pass
        else:
            can1.delete("pacman")
            can1.create_image(x, y, image=black)
            
        if direction == "Left":
            if matrix[loc[0]][loc[1]-1] == 1:
                if state == 1:
                    can1.create_image(x, y, image=left_tiny, tags="pacman")
                    state = 2
                elif state == 2:
                    can1.create_image(x, y, image=left_big, tags="pacman")
                    state = 3
                elif state == 3:
                    can1.create_image(x, y, image=closed, tags="pacman")
                    state = 1
            
                can1.move("pacman", -step,  0)
                x -= step
                loc[1] -= 1
            else:
                can1.create_image(x, y, image=closed, tags="pacman")
        
        elif direction == "Right":
            if matrix[loc[0]][loc[1]+1] == 1:
                if state == 1:
                    can1.create_image(x, y, image=right_tiny, tags="pacman")
                    state = 2
                elif state == 2:
                    can1.create_image(x, y, image=right_big, tags="pacman")
                    state = 3
                elif state == 3:
                    can1.create_image(x, y, image=closed, tags="pacman")
                    state = 1
                    
                can1.move("pacman", step,  0)
                x += step
                loc[1] += 1
            else:
                can1.create_image(x, y, image=closed, tags="pacman")
        
        elif direction == "Up":
            if matrix[loc[0]-1][loc[1]] == 1:
                if state == 1:
                    can1.create_image(x, y, image=up_tiny, tags="pacman")
                    state = 2
                elif state == 2:
                    can1.create_image(x, y, image=up_big, tags="pacman")
                    state = 3
                elif state == 3:
                    can1.create_image(x, y, image=closed, tags="pacman")
                    state = 1
                    
                can1.move("pacman", 0, -step)
                y -= step
                loc[0] -= 1
            else:
                can1.create_image(x, y, image=closed, tags="pacman")
        
        elif direction == "Down":
            if matrix[loc[0]+1][loc[1]] == 1:
                if state == 1:
                    can1.create_image(x, y, image=down_tiny, tags="pacman")
                    state = 2
                elif state == 2:
                    can1.create_image(x, y, image=down_big, tags="pacman")
                    state = 3
                elif state == 3:
                    can1.create_image(x, y, image=closed, tags="pacman")
                    state = 1
                    
                can1.move("pacman", 0,  step)
                y += step
                loc[0] += 1
            else:
                can1.create_image(x, y, image=closed, tags="pacman")
                
        
        #--- DEBUG ----#
        if x < 0 or x > mapWidth or y < 0 or y > mapHeight:
            #print("X: " + str(x) + "    Y: " + str(y) + "   Out of map !")
            print("loc: " + str(loc[0]) + "    " + str(loc[1]) + "   Out of map !")
        else:
            #print("X: " + str(x) + "    Y: " + str(y))
            print("loc: " + str(loc[0]) + "    " + str(loc[1]))
            
        time.sleep(0.09)
        

class newThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def run(self):
        print ("Starting " + self.name)
        walk()
        
        
def walk():
    global can1, matrix, state, x, y
    pass
    

fen1 = Tk()
fen1.title("PyPac")
   
bg         = PhotoImage(file="sprites/objs/bg.png")
black      = PhotoImage(file="sprites/objs/black.png")
closed     = PhotoImage(file="sprites/pacman/closed.png")
up_big     = PhotoImage(file="sprites/pacman/up_big.png")
up_tiny    = PhotoImage(file="sprites/pacman/up_tiny.png")
down_big   = PhotoImage(file="sprites/pacman/down_big.png")
down_tiny  = PhotoImage(file="sprites/pacman/down_tiny.png")
right_big  = PhotoImage(file="sprites/pacman/right_big.png")
right_tiny = PhotoImage(file="sprites/pacman/right_tiny.png")
left_big   = PhotoImage(file="sprites/pacman/left_big.png")
left_tiny  = PhotoImage(file="sprites/pacman/left_tiny.png")
   
can1 = Canvas(fen1, width=mapWidth, height=mapHeight)
can1.create_image(0, 0, anchor=NW, image=bg, tags="bg")
can1.create_image(x, y, image=left_big, tags="pacman")
can1.pack()

bou1 = Button(fen1, text='Quitter', command=quit)
bou1.pack()
   
fen1.bind_all('<Key>', keypress)

AutowalkThread = newThread(1, "Autowalk")
AutowalkThread.start()

fen1.mainloop()

print ("Exiting Main Thread")
exit()