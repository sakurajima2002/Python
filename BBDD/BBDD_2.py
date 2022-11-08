import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

""" miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))''')

productos = [

    ("PELOTA",20,"JUGUETERIA"),
    ("PANTALON",15,"COFECCION"),
    ("DESTORNILADOR",25,"FERRETERIA"),
    ("JARRON",45,"CERAMICA"),

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos) """

""" miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'COFECCION'")
productos = miCursor.fetchall()
print(productos) """

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35  WHERE ID = 1")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 4")

miConexion.commit()
miConexion.close()