import sqlite3
import csv

conexion = sqlite3.connect('/home/rei/Documentos/Python/ejemplo.db')
cursor = conexion.cursor()

archivo = open(r'/home/rei/Documentos/Python/datosdb.txt')
filas = csv.reader(archivo)

cursor.executemany('INSERT INTO estudiantes VALUES (?,?,?,?)', filas)

cursor.execute("SELECT * FROM estudiantes")
print(cursor.fetchall())

conexion.commit()
conexion.close()