#Muestras Aleatorias

import numpy as np
import pandas as pd

def CrearDataSeut(Num=1):
    Output = []
    
    for i in range(Num):
        
        #crear un rango de fechas semanal de lunes a lunes
        rango = pd.date_range(start='1/1/2016', end='12/31/2020', freq='W-Mon')
        
        #crear valores aleatorios
        data = np.random.randint(low=25, high=1000, size=len(rango))
        
        #estatus posibles
        status = [1,2,3]
        
        #lista de estatus aleatorios
        random_status = [status[np.random.randint(low=0, high=len(status))] for i in range(len(rango))]
        
        #locales posibles
        states = ['Libertador', 'El Hutillo', 'El hatillo', 'Chacao', 'Baruta', 'Sucre']
        
        #crear una lista aleatoria de estatuses
        random_states = [states[np.random.randint(low=0, high=len(states))] for i in range(len(rango))]
        
        Output.extend(zip(random_states, random_status, data, rango))
    return Output

dataset = CrearDataSeut(4)
df = pd.DataFrame(data=dataset, columns=['Local', 'Estatus_local', 'Cantidad_clientes', 'Fecha_status'])
print(df)

#np.random.choice() -> muestra aleatoria
filas = np.random.choice(df.index, 10, replace=False)
print(f'\n{filas}')
print(f'\n{df.loc[filas]}')
