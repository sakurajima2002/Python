#Arrays Especiales
import numpy as np

#zeros(filas, columnas) -> Arrays solos ceros
arreglo = np.zeros((2, 3), dtype=float)
print(arreglo) 

#ones(filas, columnas) -> Arrays solos unos
arreglo_2 = np.ones((3, 4), dtype=float)
print(f"\n{arreglo_2}")

#identity(columnas) -> matrix identidad
arreglo_3 = np.identity((4), dtype=float)
print(f"\n{arreglo_3}")

#arange(inicio, final) -> arreglo con cierto rango
arreglo_4 = np.arange(1,9)
print(f"\n{arreglo_4}")