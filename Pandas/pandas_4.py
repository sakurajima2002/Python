#Indexacion y Filtrado

import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.randint(low=0, high=10, size=(10, 2)),
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    columns=['cod_empleado', 'calificacion']
)

print(f'\n{df}')
print(f'\n{df.cod_empleado}')
print(f'\n{df["calificacion"]}')

#Selccionar con .loc
print(f'\n{df.loc["a"]}')
print(f'\n{df.loc["b":"f"]}')
print(f'\n{df.loc[df.index[3:7],"cod_empleado"]}')

#Selccionar con .iloc
print(f'\n{df.iloc[0:3]}')
print(f'\n{df.iloc[3:]}')