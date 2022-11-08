
#conjunto = set()

#conjunto = {1,2,3,"hola",4.56}

#conjunto.add(5) # add() agrega un valor  al conjunto donde quiera
#conjunto.discard(2) # discard() elimina datos del conjunto
#conjunto.clear() # clear() elimina todos los datos del conjunto

#print(3 in conjunto)
#print(11 not in conjunto)

a = {1,2,3}
b = {3,4,5}

#print(a == b)
#print(len(a))

#c = a | b #union de conjuntos
#c = a & b #interseccion de conjuntos
#c = a - b #diferencia de conjuntos
#c = b -a
#c = a ^ b #diferencia de simetrica

c = {1,2,3,4,5}
d = frozenset({7,8,9}) #conjunto inmutable

#print(c)
#print(a.issubset(c)) # issubset() para saber si un conjunto es subconjunto de otro
#print(b.issubset(c))
#print(c.issuperset(a)) #issuperset() para saber si un conjunto es un superconjunto
print(a.isdisjoint(b)) # disjoint() para saber si es un conjunto disconexo

