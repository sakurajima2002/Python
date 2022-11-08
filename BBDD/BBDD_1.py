import sqlite3

miConexion = sqlite3.connect("PrimeroBase")

miCursor = miConexion.cursor()

#Despues de crear y ejecutar el programa con la creacion de una tabla comentar linea o borrar , si no tira error
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(50))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON',15,'DEPORTES')")

""" variosProductos = [

    ("Camiseta",10,"Deportes"),
    ("Jarron",90,"Ceramica"),
    ("Camion",10,"Jugeteria")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)
"""

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall()

for producto in variosProductos:
    print(producto)

miConexion.commit() #confirmar cambios
miConexion.close()