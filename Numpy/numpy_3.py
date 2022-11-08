#Operaciones Basicas
from re import A
import numpy as np

arreglo = np.arange(1, 9) # forma -> [1,2,3,4,5,6,7,8]
arreglo.shape = (2, 4) # forma ahora con shape -> [[1,2,3,4],[5,7,6,8]]

#Suma
# arreglo += arreglo
# print(f"\n{arreglo}")

#resta
# arreglo -= arreglo
# print(f"\n{arreglo}")

#multiplicacion
# arreglo *= arreglo
# print(f"\n{arreglo}")

#potenciacion
# arreglo **= arreglo
# print(f"\n{arreglo}")

# #division
print(f"\n{arreglo / arreglo}")

