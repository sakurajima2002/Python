#Operaciones con DataFrames

import numpy as np
import pandas as pd

data = [np.random.randint(50, size=(10))]
print(data)
df = pd.DataFrame(data).T
print(f"\n{df}")

#Añadir nueva Columna
df['nueva_col'] = 10
df['experiancia'] = 5
print(f"\n{df}")
# e = numero de euler
df['perdidas'] = [(i+2)*np.e for i in range(10)]
print(f"\n{df}")
df['columna'] = df['perdidas']*100
print(f"\n{df}")

#Cambiar el nombre de una columna
print(f"\n{df.columns}")
df.columns = ['codigo_id', 'años_exp', 'indice', 'eficiencia', 'eficiencia_agregada']
print(f"\n{df}")
print(f"\n{df['codigo_id']}")

#Modificar una columna
df['indice'] = df['indice'] / 200
print(f"\n{df}")

#Eliminar columna
del(df['eficiencia'])
print(f"\n{df}")

#Descartar Fila
nueva = df.drop([2,3,5], axis=0) #0 = Filas , 1 = columnas
print(f"\n{nueva}")

#Descartar Columna
df.drop(['eficiencia_agregada'], axis=1, inplace=True) #inplace = Cambios permanentes
print(f"\n{df.head()}") #head = Trae ls 5 primeros
print(f"\n{df}")

#Modificar el indice
i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df.index = i
print(f'\n{df}')

#Media Arimetica
print(f"\n{df['codigo_id'].mean()}")

#Valor minimo
print(f"\n{df['codigo_id'].min()}")

#Valor maximo
print(f"\n{df['codigo_id'].max()}")
