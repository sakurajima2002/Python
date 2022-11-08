#Combinar conjuntos de datos

from pydoc import cli
import numpy as np
import pandas as pd

clima_p = pd.read_csv('ny_precipitaciones.csv')
print(f"\n{clima_p.shape}") #informacion de filas y columnas
print(f"\n{clima_p.head()}") 

clima_t = pd.read_csv('ny_temperaturas.csv')
print(f"\n{clima_t.shape}")
print(f"\n{clima_p.NAME}")
precip_ita = clima_p[clima_p['NAME'] ==  'MASSENA INTERNATIONAL AIRPORT, NY US']
print(f"\n{precip_ita.shape}")

#pd.merge() == innerjoin
itaca_inner_merge = pd.merge(precip_ita, clima_t)
print(f"\n{itaca_inner_merge.shape}")
print(f"\n{itaca_inner_merge.head().T}")

#outer join
itaca_inner_merge = pd.merge(precip_ita, clima_t, how='outer', on=['STATION', 'DATE'])
print(f"\n{itaca_inner_merge.columns}")
print(f"\n{itaca_inner_merge.shape}")
print(f"\n{itaca_inner_merge.head(20)}")

#left join 
itaca_inner_merge = pd.merge(precip_ita, clima_t, how='left', on=['STATION', 'DATE'])
print(f"\n{itaca_inner_merge.shape}")
print(f"\n{itaca_inner_merge}")

#right join
itaca_inner_merge = pd.merge(clima_t, precip_ita, how='right', on=['STATION', 'DATE'])
print(f"\n{itaca_inner_merge.shape}")

#join , lsuffix -> cocidencia nombre columna
clima_join = clima_t.join(clima_p, lsuffix='_left')
print(f"\n{clima_join.head()}")
print(f"\n{clima_join.columns}")
#print(f'\n{clima_p.set_index(["STATION", "DATE"])}')

clima_joined_total = clima_t.join(clima_p.set_index(["STATION", "DATE"]),
                                lsuffix="_x",
                                rsuffix="_y",
                                on=['STATION', 'DATE']
                                )

print(f"\n{clima_joined_total.head()}")

#pd.concat()
clima_total_outer_concat = pd.concat([clima_t, clima_p], axis=1)
print(f"{clima_total_outer_concat.shape}")
print(f"\n{clima_total_outer_concat.head()}")
print(f"\n{clima_total_outer_concat.tail()}")

clima_total_outer_concat = pd.concat([clima_t, clima_p], axis=0)
print(f"{clima_total_outer_concat.shape}")

df_jerar = pd.concat([clima_t, clima_p], keys=["temp", "precip"])
print(f"\n{df_jerar}")