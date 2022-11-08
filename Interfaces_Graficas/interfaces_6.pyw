from cProfile import label
from cgitb import text
from tkinter import *

raiz = Tk()

playa = IntVar()
montana = IntVar()
turismo = IntVar()

def opcionesViaje():
    opcionEscogida = ""
    if playa.get() == 1:
        opcionEscogida += " Playa "

    if montana.get() == 1:
        opcionEscogida += " Montaña "

    if turismo.get() == 1:
        opcionEscogida += " Turismo "

    texto.config(text=opcionEscogida)

frame = Frame(raiz)
frame.pack()

Label(frame, text="Elige Destino",width=50).pack()

Checkbutton(frame,text="Playa",variable=playa ,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Montaña",variable=montana,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Turismo Rural",variable=turismo,onvalue=1,offvalue=0,command=opcionesViaje).pack()

texto = Label(frame)
texto.pack()

raiz.mainloop()