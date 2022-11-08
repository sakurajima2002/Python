from tkinter import *

root = Tk()

miframe = Frame(root , width=800, height=500)
miframe.pack()

miImagen = PhotoImage(file="/home/zoro/Documentos/Python/Interfaces_Graficas/imagen.png")
#miLabel = Label(miframe,text="Hola Mundo",fg="red",font=("Comic Sans MS",18)).place(x=200,y=200) #permite ubicar el texto
Label(miframe, image=miImagen).place(x=100,y=100)

root.mainloop()