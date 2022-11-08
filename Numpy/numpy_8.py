#Transformaciones

import numpy as np

#astype -> cambiar tipo de dato del arreglo
array_1 = np.random.randint(100, size=(3,4))
print(f"\n{array_1}")
array_float = array_1.astype(float)
print(f"\n{array_float}")

#reshape > modificar dimensiones de un array
array_1 = array_1.reshape(6,2)
print(f"\n{array_1}")

#flatten -> crea un array unidimesional desde el original
plano_array = array_1.flatten()
print(f"\n{plano_array}")

#tolist -> crea una lista apartir de un array
lista_arreglo = plano_array.tolist()
print(f"\n{lista_arreglo}")

#split(arreglo, sparaciones) -> separar
array_separado = np.split(array_1, 3)
print(f"\n{array_separado}")

#concatenate((array[pocision],..), axis=eje) -> juntar , axis=(0,verticalmente),(1,horizontalmente)
array_junto = np.concatenate((array_separado[1], array_separado[0]), axis=0)
print(f"\n{array_junto}")

# T = matriz transpuesta 
array_2 = array_1.T
print(f"\n{array_2}")