#Algebra lineal

import numpy as np

#Producto de Arrays
array_1 = np.array([1, 2, 3], float)
array_2 = np.array([0, 1, 1], float)
print(np.dot(array_1, array_2)) #Producto escalar

#Producto de Matrices
# array_3 = np.array([[5, 2], [4, 8]], float)
# array_4 = np.array([[2, 4], [5, 3]], float)
# print("\n---------")
# print(array_3,"\n---------")
# print(array_4,"\n---------")
# print(np.dot(array_3, array_4))

#Producto de Matrices
array_3 = np.array([[5, 2], [4, 8]], float)
array_4 = np.array([[2, 4], [5, 3]], float)
print("\n---------")
print(array_3 @ array_4)

#Producto de array unidimensional y multidimensional
array_5 = np.array([[0, 1, 4], [5, 2, 3], [1, 4, 8]], float)
array_6 = np.array([2, 1, 5], float)
print("\n---------")
print(array_5,"\n---------")
print(array_6,"\n---------")
print(array_5 @ array_6)
print(np.matmul(array_5, array_6))

#Determinante de una matriz
print("\n---------")
array_7 = np.array([[8, 5], [3, 4]])
print(array_7,"\n---------")
print(np.linalg.det(array_7))

#Auto valores y Auto vectores
array_8 = np.array([[8, 5], [3, 4]])
valores , vectores = np.linalg.eig(array_8)
print("\n---------")
print(valores,"\n---------")
print(vectores,"\n---------")