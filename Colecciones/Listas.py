
lista1 = [1,6,8,0,5,"Juan"]
lista2 = [4,6,2,5,3,1]

#lista1.append("Juan") # append() agrega elementos al final de la lista
#lista1.insert(2,2.5) # insert(posicion,dato) agrega un elemento en una pocicion especifica
#lista1.extend([6,7,8]) #extend() agrega una lista a otra
#lista1.pop(4) # pop() elimina un elemento de una lista ingresando el indixe del dato
#lista1.remove(3) # remove() elimina un elemento de la lista pasando el valor del elemento
#lista1.clear() # clear() eliminar toda la lista
#lista1.reverse() # reverse() pone la lista en orden inverso
#lista2.sort() #sort() ordena los datos de forma ascendente
lista2.sort(reverse=True) # ordena los datos de forma decsendente

#print(len(lista1)) #len() Cantidad de elementos de la lista
#print("Juan" in lista1) #Saber si un dato se encuentra en la lista
#print(lista1.index(5)) # index(5) encuentra el indice donde se encuentra el dato
#print(lista1.count("Juan")) # count() cuenta cuantas veces se encuentra un dato en la lista

print(lista1)
print(lista2)
