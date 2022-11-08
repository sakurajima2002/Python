import numpy as np
import pandas as pd

#Crear una series con idices automaticos
serie = pd.Series([1979, 1980, 1981, 1982])
print(f"{serie}")
print(f"\n{serie.values}")
print(f"\n{serie.values.sum()}")
print(f"\n{serie.index}")

#Podemos definir explicitamente un array indice y pasarlo como argumento
serie = pd.Series([1990, 1991, 1992, 1993], index=['daniela', 'andrea', 'valentina', 'genesis'])
print(f"\n{serie}")
print(f"\n{serie.index}")

#Podemos crear Series a partir de diccionarios, arrays, ect
serie = pd.Series(np.random.rand(10))
print(f"\n{serie}")

diccionario = {f'cuadrado de {i}': i*i for i in range(11)}
print(f"\n{diccionario}")

serie_dicc = pd.Series(diccionario)
print(f"\n{serie_dicc}")