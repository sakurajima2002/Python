"""

Escriba un programa donde tenga una lista y que, a continuacion
elimine los elementos repetidos de la lista , por ultimo
mostrar lista

"""

lista = [1,2,3,3,4,1]

lista = list(set(lista))

print(lista)
