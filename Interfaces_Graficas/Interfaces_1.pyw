from tkinter import *

raiz = Tk()

raiz.title("Ventana de Pruebas") #titulo
raiz.resizable(True,True) #  (ancho,alto)
#raiz.geometry("650x350") #tamaño de ventana por defecto
raiz.config(bg="grey") #color de fondo
raiz.config(bd=20)
raiz.config(relief="groove")
raiz.config(cursor="hand2")

miframe = Frame()
#miframe.pack(side="right",anchor="n") #empaquetar el frame a la raiz  , side y anchor = para redicerionamiento
#miframe.pack(fill="both", expand="True") #fill redirecionar frame
miframe.pack()
miframe.config(bg="white")
miframe.config(width="650",height="350") #tamaño del frame
miframe.config(bd=10) #cambiar grueso del borde
miframe.config(relief="sunken") #agregar borde
miframe.config(cursor="pirate") #cambiar cursor

raiz.mainloop()