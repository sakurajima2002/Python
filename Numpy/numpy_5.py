#Funciones Universales Unarias

import numpy as np


#Comparaciones
# [elemto1 , elemento2] -> array 1
# [elemto1 , elemento2] -> array 2
# [comparacion1 , comparacion2]

array_1 = np.array([2, 4, 9], float)
print(np.sqrt(array_1)) #Raiz Cuadrada de cada elemento del array
print(np.exp(array_1)) #Exponencial
print(np.log(array_1)) #Logaritmo natural
print(np.sin(array_1)) #Seno
print(np.cos(array_1)) #Coseno
print(np.mean(array_1)) #Media -> (2 + 4 + 9)/3