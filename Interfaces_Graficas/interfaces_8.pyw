from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir",initialdir="/home/zoro",filetypes=(("Texto","*.txt"),
            ("Ficheros Excel","*.xlsx"),("Todos los Ficheros","*.*")))
    print(fichero)

Button(root, text="AbrirFichero",command=abreFichero).pack()

root.mainloop()