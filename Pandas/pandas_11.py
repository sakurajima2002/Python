#Operaciones sobre datos agrupados
import numpy as np
import pandas as pd

ratings = pd.read_csv('ratings.csv')
peliculas = pd.read_csv('peliculas.csv')
usuarios = pd.read_csv('usuarios.csv')

print(f"\n{ratings.columns}")
print(f"\n{ratings.head()}")

print(f"\n{peliculas.columns}")
print(f"\n{peliculas.head()}")

print(f"\n{usuarios.columns}")
print(f"\n{usuarios.head()}")

""" 
Un rating requiere un usuario y una pelicula, y los
DataFrames estan vinculados por una clave (en este caso
la clave es user_id y peli_id .)

Es posible que un usuario este asociado con 0 o varios
ratings y peliculas. De la misma forma, una pelicula puede
tener muchos ratings o ninguno por un numero de diferencias 
usuarios
"""

peli_ratings = pd.merge(peliculas, ratings)
clasif = pd.merge(peli_ratings, usuarios)

mas_ratings = clasif.groupby('titulo').size().sort_values(ascending=False)[:25]
print(f"\n{mas_ratings}")

#.agg()
peli_status = clasif.groupby('titulo').agg({'rating': [np.size, np.mean]})
print(f"\n{peli_status.head()}")

#Peliculas con mayor rating
print(f"\n{peli_status.sort_values([('rating', 'mean')], ascending=False).head()}")

#Peliculas con mas de 100 vistas
minimo_100 = peli_status['rating']['size'] >= 100
print(f"\n{minimo_100}")
print(f"\n{peli_status[minimo_100].sort_values([('rating', 'mean')], ascending=False)[:25]}")