import sqlite3

conexion = sqlite3.connect('ejemplo.db')
cursor = conexion.cursor()

#cursor.execute('CREATE TABLE estudiantes (email VARCHAR(100), carrera VARCHAR(100), nombre VARCHAR(100), edad INTEGER)')

cursor.execute('INSERT INTO estudiantes VALUES ("juanse63@gmail.com", "Sistemas", "Sebastian Laverde",19)')

# cursor.execute('SELECT * FROM estudiantes')
# usuarios = cursor.fetchone() #Obtener un dato -> fetchone
# print(usuarios)

usuarios = [
    ('carlos@gmail.com','Calculo','Carlos Perez',20),
    ('maria@gmail.com','Diseño','Maria Feria',22),
    ('antonio@gmail.com','Informatica','Antonio Sans',19)
]

cursor.executemany('INSERT INTO estudiantes VALUES (?,?,?,?)',usuarios)

cursor.execute("SELECT * FROM estudiantes")
usuarios = cursor.fetchall() # fetchall -> toma todos

for usuario in usuarios:
    print(usuario)

conexion.commit()
conexion.close()