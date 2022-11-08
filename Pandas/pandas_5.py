#Fechas con Pandas
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta

#.to_datetime()
fecha = pd.to_datetime('24th April, 2020')
print(fecha)
print(type(fecha))
print(fecha.year)

#.to_timedelta()
fecha = datetime.datetime.now()
print(f"\nLa fecha de hoy es: {fecha}")
print(f"La Fecha en 4 dias sera: {fecha + pd.to_timedelta(4, unit='D')}") #unit = 'D' -> Dias

#.date_range()
fecha_inicio = pd.date_range(start='24/4/2020', end='24/5/2020', freq='D') #freq -> 'D' -> Frecuencia Diaria
print(f"\n{fecha_inicio}")

fecha_fin = pd.date_range(start='24/5/2020', end='24/6/2020', freq='D') 
print(f"\n{fecha_fin}")

lista_equis = []
for i in range(15):
    lista_equis.append(np.random.randint(2))

df = pd.DataFrame()
df["Inicio_campaña"] = fecha_inicio[:15]
df["Fin_campaña"] = fecha_fin[:15]
df["Target"] = lista_equis
print(f"\n{df}")

df['Dia_inicio'] = df['Inicio_campaña'].dt.day
df['Mes_inicio'] = df['Inicio_campaña'].dt.month
df['Año_inicio'] = df['Inicio_campaña'].dt.year
df['Hora_inicio'] = df['Inicio_campaña'].dt.hour
df['Minuto_inicio'] = df['Inicio_campaña'].dt.minute
df['Segundo_inicio'] = df['Inicio_campaña'].dt.second
df['Nombre del dia de inicio'] = df['Inicio_campaña'].dt.weekday
df['Semana_inicio'] = df['Inicio_campaña'].dt.week
df['Duracion'] = df['Fin_campaña']- df['Inicio_campaña']
print(f"\n{df}")

df.columns = [
    'Inicio_campaña',
    'Fin_campaña',
    'Target',
    'Dia_inicio',
    'Mes_inicio',
    'Año_inicio',
    'Hora_inicio',
    'Minuto_inicio',
    'Segundo_inicio',
    'Dia_inicio',
    'Semana_inicio',
    'Duracion'
    ]

print(f"\n{df}")

#timedelta
df['Dias_duracion'] = df['Duracion']/timedelta(days=1)
df['Minutos_duracion'] = df['Duracion']/timedelta(minutes=1)
df['Segundos_duracion'] = df['Duracion']/timedelta(seconds=1)
print(f"\n{df}")