#Funciones Universales Binarias

import numpy as np

array_1 = np.array([5, 36, 17, 18, 9])
array_2 = np.array([8, 24, 17, 19, 9])

#Comparaciones
# [elemto1 , elemento2] -> array 1
# [elemto1 , elemento2] -> array 2
# [comparacion1 , comparacion2]

print(np.add(array_1, array_2)) #Suma entre los dos arrays
print(np.subtract(array_1, array_2)) #Resta
print(np.multiply(array_1, array_2)) #Multiplicar
print(np.divide(array_1, array_2)) #Division
print(np.array_equal(array_1, array_2)) #Si los arreglos son iguales
print(np.fmin(array_1, array_2)) #Numeros Minimos
print(np.fmax(array_1, array_2)) #Numeros Maximos