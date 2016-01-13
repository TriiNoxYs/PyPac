#!/usr/bin/python

#GIT TEST

import threading
import time
from tkinter import *  # @UnusedWildImport
from tkinter.messagebox import askyesno

direction = "None"
state = 1
x = 249
y = 412
mapWidth  = 398
mapHeight = 498
blocked = False

def quit():  #@ReservedAssignment
    if askyesno('Quitter', 'Êtes-vous sûr de vouloir quitter ?'):
        fen1.destroy()
        #AutowalkThread.Exit()
 
def keypress(event):
    global can1, direction
    if event.keysym == "Left":  
        can1.move("pacman",-5,  0)
        direction = "Left"
        
    elif event.keysym == "Right": 
        can1.move("pacman", 5,  0)
        direction = "Right"
        
    elif event.keysym == "Up":    
        can1.move("pacman", 0, -5)
        direction = "Up"
        
    elif event.keysym == "Down":  
        can1.move("pacman", 0,  5)
        direction = "Down"
    
    elif event.keysym == "Escape":  
        quit()
        

class newThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        #self.counter = counter
        
    def run(self):
        print ("Starting " + self.name)
        walk()
        
def walk():
    global can1, state, x, y
    while True:
        can1.delete("pacman")
        #can1.create_image(x, y, image=closed)   A FUCKING SNAKE GAME !!!
        
        if direction == "None":
            can1.create_image(x, y, image=closed, tags="pacman")
        
        elif direction == "Left":
            if state == 1:
                can1.create_image(x, y, image=left_tiny, tags="pacman")
                state = 2
            elif state == 2:
                can1.create_image(x, y, image=left_big, tags="pacman")
                state = 3
            elif state == 3:
                can1.create_image(x, y, image=closed, tags="pacman")
                state = 1
            can1.move("pacman",-5,  0)
            x -= 5
        
        elif direction == "Right":
            if state == 1:
                can1.create_image(x, y, image=right_tiny, tags="pacman")
                state = 2
            elif state == 2:
                can1.create_image(x, y, image=right_big, tags="pacman")
                state = 3
            elif state == 3:
                can1.create_image(x, y, image=closed, tags="pacman")
                state = 1
            can1.move("pacman", 5,  0)
            x += 5
        
        elif direction == "Up":
            if state == 1:
                can1.create_image(x, y, image=up_tiny, tags="pacman")
                state = 2
            elif state == 2:
                can1.create_image(x, y, image=up_big, tags="pacman")
                state = 3
            elif state == 3:
                can1.create_image(x, y, image=closed, tags="pacman")
                state = 1
            can1.move("pacman", 0, -5)
            y -= 5
        
        elif direction == "Down":
            if state == 1:
                can1.create_image(x, y, image=down_tiny, tags="pacman")
                state = 2
            elif state == 2:
                can1.create_image(x, y, image=down_big, tags="pacman")
                state = 3
            elif state == 3:
                can1.create_image(x, y, image=closed, tags="pacman")
                state = 1
            can1.move("pacman", 0,  5)
            y += 5
            
        #--- DEBUG ----#
        if x < 0 or x > 498 or y < 0 or y > mapHeight:
            print("X: " + str(x) + "    Y: " + str(y) + "   Out of map !")
            #blocked = True
        else:
            print("X: " + str(x) + "    Y: " + str(y))
        
            
        time.sleep(0.05)
    

fen1 = Tk()
fen1.title("PyPac")
   
bg         = PhotoImage(file="sprites/objs/new_bg.png")
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
can1.create_image(x, y, image=closed, tags="pacman")
can1.pack()

bou1 = Button(fen1, text='Quitter', command=quit)
bou1.pack()
   
fen1.bind_all('<Key>', keypress)

AutowalkThread = newThread(1, "Autowalk")
AutowalkThread.start()

fen1.mainloop()

print ("Exiting Main Thread")