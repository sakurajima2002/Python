#Arrays Multidimensionales
#Instalacion pip install numpy
import numpy as np

#Array unidimensional
arreglo = np.array([0,1,2,3,4,5])
print(arreglo, type(arreglo))

notas = [50, 40, 30, 40]
arreglo_notas = np.array(notas, dtype=float)
print(arreglo_notas, type(arreglo_notas[0]))

#Array multidimensional
print("\nArreglo Multidimensional")
array_notas_todas = np.array(([35, 50, 42, 50], notas))
print(array_notas_todas)
print("Dimiensiones: ",array_notas_todas.ndim) # ndin -> saber cuantas dimensiones tiene
print("Tamaño cada Dimension: ", array_notas_todas.shape)