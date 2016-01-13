#!/usr/bin/python

import threading
import time
from tkinter import *  # @UnusedWildImport
from tkinter.messagebox import askyesno  # @UnusedWildImport @Reimport
from asyncio.tasks import sleep

dir = "None"
state = 1
x = 249
y = 412
mapHeight = 544
mapWidth  = 498
blocked = False

def quit():  #@ReservedAssignment
    if askyesno('Quitter', 'Etes-vous sur de vouloir quitter ?'):
        fen1.destroy()
        #AutowalkThread.Exit()
 
def keypress(event):
    global can1, dir
    if event.keysym == "Left":  
        can1.move("pacman",-5,  0)
        dir = "Left"
        
    elif event.keysym == "Right": 
        can1.move("pacman", 5,  0)
        dir = "Right"
        
    elif event.keysym == "Up":    
        can1.move("pacman", 0, -5)
        dir = "Up"
        
    elif event.keysym == "Down":  
        can1.move("pacman", 0,  5)
        dir = "Down"
    
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
        
        if dir == "None":
            can1.create_image(x, y, image=closed, tags="pacman")
        
        elif dir == "Left":
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
        
        elif dir == "Right":
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
        
        elif dir == "Up":
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
        
        elif dir == "Down":
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
   
bg         = PhotoImage(file="sprites/objs/bg.png")
closed     = PhotoImage(file="sprites/pacman/closed.png")
up_big     = PhotoImage(file="sprites/pacman/up_big.png")
up_tiny    = PhotoImage(file="sprites/pacman/up_tiny.png")
down_big   = PhotoImage(file="sprites/pacman/down_big.png")
down_tiny  = PhotoImage(file="sprites/pacman/down_tiny.png")
right_big  = PhotoImage(file="sprites/pacman/right_big.png")
right_tiny = PhotoImage(file="sprites/pacman/right_tiny.png")
left_big   = PhotoImage(file="sprites/pacman/left_big.png")
left_tiny  = PhotoImage(file="sprites/pacman/left_tiny.png")
   
can1 = Canvas(fen1, width=500, height=546)
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