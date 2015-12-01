from tkinter import *

def key(event):
    if event.char == event.keysym:
        msg = 'Normal Key %r' % event.char
    elif len(event.char) == 1:
        msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
    else:
        msg = 'Special Key %r' % event.keysym
    print(msg)

fen1 = Tk()
fen1.title("Test keypress")

fen1.bind_all('<Key>', key)

fen1.mainloop()

