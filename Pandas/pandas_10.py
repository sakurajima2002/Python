#Agrupar Datos
import numpy as np
import pandas as pd

data = pd.read_csv('data_celular.csv',
                header=0, #Si contiene los nombre de las columnas
                index_col=0, #indicar columna indice
                names=['indice','fecha','duracion','item','mes','red','tipo_red'],
                parse_dates=['fecha']) #Indica columna fecha sea tipo datetime

print(f"\n{data.head()}")

print("\nCuantas filas tiene el DataFrame: ",data['item'].count())

print("El tiempo total (en segundos) registrado en llamada es: ",
    data['duracion'][data['item'] == 'call'].sum())

print("Con cuantas redes telefonicas se contacto en el periodo de 2014/11 al 2015/03: ",
    data['red'].nunique())

#.groupby()
print(f"\n{data.groupby('mes').groups.keys()}")
print(f"\n{data.groupby('mes').sum()}")

print('''\nEn el siguiente cuadro veremos la cantidad de entradas por mes
agregadas en llamadas, sms y datos: ''')
print("\n",data.groupby(['mes', 'item'])['duracion'].count())

print("\nLa duracion total de las llamadas realizadas a cada una de las operadoras es: ")
print(f"\n{data[data['item'] == 'call'].groupby('red')['duracion'].sum()}")

print("\n¿Cuantas llamadas, sms y datos son enviados a cada operador por mes?")
print(f"\n{data.groupby(['mes', 'tipo_red'])['fecha'].count()}")