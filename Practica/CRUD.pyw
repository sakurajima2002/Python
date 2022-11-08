from tkinter import *
from tkinter import messagebox
import sqlite3

#----------------------Funciones--------------------

def conexionBBDD():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()

    try:
        micursor.execute('''
            CREATE TABLE DATOS_USUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO_USUARIOS VARCHAR(50),
                DIRECCION_USUARIOS VARCHAR(50),
                COMENTARIO VARCHAR(100))
                ''')

        messagebox.showinfo("BBDD","BBDD creada con exito")

    except:

        messagebox.showinfo("¡Atencion!","BBDD ya existe")

def salirAPP():
    valor = messagebox.askquestion("Salir","¿Desea Salir?")
    if valor == "yes":
        root.destroy()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    cuadroComentario.delete(1.0,END)

def CREATE():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()

    """ micursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,'"+miNombre.get()+
    "','"+miPass.get()+
    "','"+miApellido.get()+
    "','"+miDireccion.get()+
    "','"+cuadroComentario.get("1.0",END) + "')") """

    datos = miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),cuadroComentario.get("1.0",END)
    micursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)",(datos))

    miconexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito")

def READ():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()

    micursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID =" + miId.get() )
    elUsuario = micursor.fetchall()
    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        cuadroComentario.insert(1.0, usuario[5])

    miconexion.commit()

def UPDATE():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()

    """ micursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO='"+miNombre.get()+
        "',PASSWORD='"+miPass.get()+
        "',APELLIDO_USUARIOS='"+miApellido.get()+
        "',DIRECCION_USUARIOS='"+miDireccion.get()+
        "',COMENTARIO='"+cuadroComentario.get(1.0,END)+
        "' WHERE ID="+miId.get()) """

    datos = miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),cuadroComentario.get("1.0",END)
    micursor.execute('''
        UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO=?,
        PASSWORD=?,APELLIDO_USUARIOS=?,DIRECCION_USUARIOS=?,
        COMENTARIO=? WHERE ID='''+miId.get(),(datos))

    miconexion.commit()
    messagebox.showinfo("BBDD","Registro Actualizado con exito")

def DELETE():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()

    valor = messagebox.askquestion("BBDD","¿Estas Seguro de eliminar el ususario?")
    if valor == "yes":
        micursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID="+ miId.get())
        miconexion.commit()
        messagebox.showinfo("BBDD","Usuario eliminado")

def informacionAPP():
    messagebox.showinfo("Formulario Sebas","Formulario Usuarios 2022")

def licenciaAPP():
    messagebox.showinfo("Licencia","Producto bajo licencia GNU")

root = Tk()

barraMenu = Menu(root,font=("Comic Sans MS",10))
barraMenu.config(bg="gray",fg="black")
root.config(menu=barraMenu,width=300,height=300)

bbddMenu = Menu(barraMenu,tearoff=0)
bbddMenu.config(bg="gray")
bbddMenu.add_command(label="Conectar",command=conexionBBDD,font=("Comic Sans MS",10))
bbddMenu.add_command(label="Salir",command=salirAPP,font=("Comic Sans MS",10))

borrarMenu = Menu(barraMenu,tearoff=0)
borrarMenu.config(bg="gray")
borrarMenu.add_command(label="Borrar Campos",command=limpiarCampos,font=("Comic Sans MS",10))

crudMenu = Menu(barraMenu,tearoff=0)
crudMenu.config(bg="gray")
crudMenu.add_command(label="CREATE",command=CREATE,font=("Comic Sans MS",10))
crudMenu.add_command(label="READ",command=READ,font=("Comic Sans MS",10))
crudMenu.add_command(label="UPDATE",command=UPDATE,font=("Comic Sans MS",10))
crudMenu.add_command(label="DELETE",command=DELETE,font=("Comic Sans MS",10))

ayudaMenu = Menu(barraMenu,tearoff=0)
ayudaMenu.config(bg="gray")
ayudaMenu.add_command(label="Licencia",command=licenciaAPP,font=("Comic Sans MS",10))
ayudaMenu.add_command(label="Acerca De",command=informacionAPP,font=("Comic Sans MS",10))

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#--------------------Comienzo de Campos----------------------------

miframe = Frame(root)
miframe.pack()

miId = StringVar()
miNombre = StringVar()
miPass = StringVar()
miApellido = StringVar()
miDireccion = StringVar()

cuadroId = Entry(miframe,textvariable=miId,font=("Comic Sans MS",10))
cuadroId.grid(row=0,column=1,padx=10,pady=10)
cuadroId.config(justify="center",bg="gray")

cuadroNombre = Entry(miframe,textvariable=miNombre,font=("Comic Sans MS",10))
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(justify="center",bg="gray")

cuadroContraseña = Entry(miframe,textvariable=miPass,font=("Comic Sans MS",10))
cuadroContraseña.grid(row=2,column=1,padx=10,pady=10)
cuadroContraseña.config(show="*",justify="center",bg="gray")

cuadroApellido = Entry(miframe,textvariable=miApellido,font=("Comic Sans MS",10))
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)
cuadroApellido.config(justify="center",bg="gray")

cuadroDireccion = Entry(miframe,textvariable=miDireccion,font=("Comic Sans MS",10))
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)
cuadroDireccion.config(justify="center",bg="gray")

cuadroComentario = Text(miframe , width=16,height=5,font=("Comic Sans MS",10))
cuadroComentario.grid(row=5,column=1,padx=10,pady=10)
scrollVert = Scrollbar(miframe,command=cuadroComentario.yview)
scrollVert.grid(row=5,column=3,sticky="nsew")
cuadroComentario.config(yscrollcommand=scrollVert.set,bg="gray")

#--------------------Labels---------------------------------------------

idlabel = Label(miframe,text="ID:",font=("Comic Sans MS",10))
idlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombrelabel = Label(miframe,text="Nombre:",font=("Comic Sans MS",10))
nombrelabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passlabel = Label(miframe,text="Contraseña:",font=("Comic Sans MS",10))
passlabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

apellidolabel = Label(miframe,text="Apellido:",font=("Comic Sans MS",10))
apellidolabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionlabel = Label(miframe,text="Direccion:",font=("Comic Sans MS",10))
direccionlabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comenlabel = Label(miframe,text="Comentario:",font=("Comic Sans MS",10))
comenlabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#--------------------Botones---------------------------------------------

miframe2 = Frame(root)
miframe2.pack()

botonCrear = Button(miframe2,text="Crear",command=CREATE,font=("Comic Sans MS",10))
botonCrear.grid(row=0,column=0,sticky="e",padx=10,pady=10)
botonCrear.config(bg="gray")

botonLeer = Button(miframe2,text="Leer",command=READ,font=("Comic Sans MS",10))
botonLeer.grid(row=0,column=1,sticky="e",padx=10,pady=10)
botonLeer.config(bg="gray")

botonActualizar = Button(miframe2,text="Actualizar",command=UPDATE,font=("Comic Sans MS",10))
botonActualizar.grid(row=0,column=2,sticky="e",padx=10,pady=10)
botonActualizar.config(bg="gray")

botonBorrar = Button(miframe2,text="Borrar",command=DELETE,font=("Comic Sans MS",10))
botonBorrar.grid(row=0,column=3,sticky="e",padx=10,pady=10)
botonBorrar.config(bg="gray")

root.mainloop()
