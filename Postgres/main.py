import psycopg2

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="sebas2019",
    database="python",
    port="5432"
)

connection.autocommit = True

def crearTabla():
    cursor = connection.cursor()
    query = "CREATE TABLE usuario(nombre VARCHAR(30), correo VARCHAR(30), telefono NUMERIC(10))"
    try:    
        cursor.execute(query)
        cursor.close()
    except:
        print("La tabla ya existe")

def insertarDatos(nombre, correo, telefono):
    cursor = connection.cursor()
    query = f""" INSERT INTO usuario (nombre, correo, telefono) VALUES ('{nombre}', '{correo}', {telefono})"""
    cursor.execute(query)
    cursor.close()

def actualizarDatos():
    cursor = connection.cursor()
    query = f""" UPDATE usuario  SET nombre='Sebastian' WHERE nombre='Juan' """
    cursor.execute(query)
    cursor.close()

def eliminarTabla():
    cursor = connection.cursor()
    query = "DROP TABLE usuario"
    cursor.execute(query)
    cursor.close()

#crearTabla()
insertarDatos('Juan', 'juan@gmail.com', 1234567890)
#actualizarDatos()
#eliminarTabla()
