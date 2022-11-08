import re

lista = ['Ma1',
         'Se1',
         'Ma2',
         'Ba1',
         'Ma:3',
         'Va1',
         'Va2',
         'Ma4',
         'MaA',
         'Ma.5',
         'MaB',
         'Ma:C']

for element in lista:
    if re.findall('Ma[.:]',element):
        print(element)