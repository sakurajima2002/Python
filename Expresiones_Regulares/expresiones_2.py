import re

""" lista_nombres = ['Ana Gomez' ,
                 'Maria Martin',
                 'Sandra Lopez',
                 'Santiago Martin',
                 'Sandra Fernandez']

for elemento in lista_nombres:
    if re.findall('^Sandra',elemento):
        print(elemento)
    if re.findall('Martin$',elemento):
        print(elemento)
 """

dominios = ['http://www.pildoras.es',
            'ftp://www.pildoras.es',
            'http://www.pildoras.com',
            'ftp://www.pildoras@.com',
            'http://informaticaespaña.es',
            'niños',
            'niñas',
            'hombres',
            'mujeres',
            'camion',
            'camión']

for elemento in dominios:
    if re.findall('^ftp',elemento):
        print(elemento)

    if re.findall('[@]',elemento):
        print(elemento)

    if re.findall('niñ[oa]s',elemento):
        print(elemento)

    if re.findall('cami[oó]n',elemento):
        print(elemento)