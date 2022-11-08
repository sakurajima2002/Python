#Indexacion y slicing

import numpy as np

array_1 = np.array(range(64)).reshape((8, 8))
print(array_1)

#Indexar = [filas , elementos_contenidos_filas]
print(f"\n{array_1[1,1]}")
print(f"\n{array_1[0:7:2,0:4]}")
print(f"\n{array_1[1,3:]}")
print(f"\n{array_1[[1,3,5],[3,6,7]]}")
print(f"\n{array_1[[1,3,5],::3]}")

#Indexacion Boolean
data = np.arange(8)
print(f"\n{data}")
print(f"{data < 4}")
print(f"{data[data<4]}")

amigos = np.array(['juan', 'carlos', 'andres'])
print(f"\n{'juan' in amigos}")
print(f"{amigos['juan' != amigos]}")