
lista = ['a', 'b', 'c', 'd', 'e', 'f']
lista2 = ['a', 'b', 'c', 'h', 'g']

lista = set(lista)
lista2 = set(lista2)

lista3 = list(lista | lista2)
print(f"Elementos que aparecen  en las dos listas {lista3}")

lista3 = list(lista - lista2)
print(f"Elemetos de la primera lista que no aparecen en la segunda {lista3}")

lista3 = list(lista2 - lista)
print(f"Elemetos de la segunda lista que no aparecen en la primera {lista3}")

lista3 = list(lista & lista2)
print(f"Elementos que aparecen en ambas listas {lista3}")