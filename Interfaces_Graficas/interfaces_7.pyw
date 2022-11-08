from tkinter import *
from tkinter import messagebox

root = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador Sebas", "Procesador Textos 2022")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def salir():
    valor = messagebox.askquestion("Salir","¿Deseas Salir de la aplicacion?")

    if valor == "yes":
        root.destroy()

def guardar():
    valor = messagebox.askokcancel("Guardar","¿Deseas Guardar Cambios?")

    if valor == True:
        messagebox.showinfo("Guardado","Cambios Guardados")

def cerrar():
    valor = messagebox.askretrycancel("Reintentar","No es posible cerrar")

    if valor == False:
        root.destroy()

barraMenu = Menu(root)
root.config(menu=barraMenu ,width=300,height= 300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar",command=guardar)
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrar)
archivoMenu.add_command(label="Salir",command=salir)

archivoEdit = Menu(barraMenu, tearoff=0)
archivoEdit.add_command(label="Cortar")
archivoEdit.add_command(label="Copiar")
archivoEdit.add_command(label="Pegar")

archivoTools = Menu(barraMenu , tearoff=0)

archivoHelp = Menu(barraMenu , tearoff=0)
archivoHelp.add_command(label="Licencia",command=avisoLicencia)
archivoHelp.add_command(label="Acerca De",command=infoAdicional)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edit",menu=archivoEdit)
barraMenu.add_cascade(label="Tools",menu=archivoTools)
barraMenu.add_cascade(label="Help",menu=archivoHelp)

root.mainloop()