from tkinter import *

def codigoBoton():
    minombre.set("Juan")

root = Tk()

miframe = Frame(root , width=1200, height=600)
miframe.pack()

minombre = StringVar()

textoNombre = Entry(miframe,font=("Comic Sans MS",10),textvariable=minombre)
textoNombre.grid(row=0, column=1,padx=10)
textoNombre.config(fg="gray",justify="center")

textoApellido = Entry(miframe,font=("Comic Sans MS",10))
textoApellido.grid(row=1, column=1,padx=10)
textoApellido.config(fg="gray",justify="center")

textoContraseña = Entry(miframe,font=("Comic Sans MS",10))
textoContraseña.grid(row=2, column=1,padx=10)
textoContraseña.config(show="*")
textoContraseña.config(fg="gray",justify="center")

textoComentario = Text(miframe,width=16,height=5,font=("Comic Sans MS",10))
textoComentario.grid(row=4,column=1,sticky="nsew")

scroll = Scrollbar(miframe, command=textoComentario.yview)
scroll.grid(row=4,column=2)
textoComentario.config(yscrollcommand=scroll.set)

textoDireccion = Entry(miframe,font=("Comic Sans MS",10))
textoDireccion.grid(row=3, column=1,padx=20)
textoDireccion.config(fg="gray",justify="center")

labelNombre = Label(miframe,text="Nombre: ",font=("Comic Sans MS",10))
labelNombre.grid(row=0, column=0,sticky="e",padx=20,pady=10)

labelApellido = Label(miframe,text="Apellido: ",font=("Comic Sans MS",10))
labelApellido.grid(row=1, column=0,sticky="e",padx=20,pady=10)

labelContraseña = Label(miframe,text="Contraseña: ",font=("Comic Sans MS",10))
labelContraseña.grid(row=2, column=0,sticky="e",padx=20,pady=10)

labelDireccion= Label(miframe,text="Direccion: ",font=("Comic Sans MS",10))
labelDireccion.grid(row=3, column=0,sticky="e",padx=20,pady=10)

labelComentarios= Label(miframe,text="Comentarios: ",font=("Comic Sans MS",10))
labelComentarios.grid(row=4, column=0,sticky="e",padx=20,pady=10)

boton = Button(miframe,text="Enviar",command=codigoBoton)
boton.grid(row=5, column=1,padx=8)

root.mainloop()