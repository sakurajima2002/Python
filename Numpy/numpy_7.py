#Agregar y Quitar valores a un Array

import numpy as np

array_1 = np.arange(0, 20, 2)
print(array_1)

#rand(filas, columnas) -> numeros aleatorios entre 0 y 1 
array_2 = np.random.rand(4, 3)
print(f"\n{array_2}")

#randint(limite, size=(filas, columnas)) -> numeros aleatorios entre el rango establecido
array_3 = np.random.randint(10, size=(2, 3))
print(f"\n{array_3}")

#full((filas, columnas), numero) -> arreglo de solo el numero establecido
array_4 = np.full((3, 3), 6)
print(f"\n{array_4}")

#append(arreglo, valores _agregar) -> Agregar al final
array_1 = np.append(array_1, [13, 14, 51])
print(f"\n{array_1}")

#insert(arreglo, posicion_agregar, valores_agregar) -> Agregar en cierta posicion
array_1 = np.insert(array_1, 2, [43, 44])
print(f"\n{array_1}")

array_4 = np.insert(array_4, 3, [1, 2, 3])
print(f"\n{array_4}")

#delete(arreglo, posicion_eliminar, axis=eje) -> Eliminar
np.delete(array_1, 2, axis=0)
print(f"\n{array_1}")

array_3 = np.delete(array_3, 2, axis=1)
print(f"\n{array_3}")