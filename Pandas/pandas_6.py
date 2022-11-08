#Manejo de datos ausentes
import numpy as np
import pandas as pd

df = pd.DataFrame({
    
    'varA' : ['aa', None, 'cc'],
    'varB' : [20, 30, None],
    'varC' : [1254, 1456, 6709],
    },
    
    index = ['Caso 1', 'Caso 2', 'Caso 3']
    
    )

print(f'\n{df}')

#pd.isnull(df) -> ver si existen valores nulos
print(f'\n{pd.isnull(df)}')

#Alternativas Para valores nulos

#dropnap(subset='subconjunto') -> descartafr valores nulos
#print(f'{df.dropna(subset=["varA", "varB"])}')

#.fillna(cualquier_valor) -> llenar nulos
print(f'\n{df.fillna(23)}')

#llenar nulos con .fillna() y media aritmetica de la columna
#print(f'\n{df.fillna(df.mean())}')
