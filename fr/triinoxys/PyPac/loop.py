from fr.triinoxys.PyPac.main import *  # @UnusedWildImport

def agiot():
    global mode, can1
    while True:
        if (mode == "none"): print("marche !")
        if (mode == "Left"):  can1.move("pacman",-5, 0)
        if (mode == "Right"): can1.move("pacman", 5, 0)
        if (mode == "Up"):    can1.move("pacman", 0,-5)
        if (mode == "Down"):  can1.move("pacman", 0, 5)