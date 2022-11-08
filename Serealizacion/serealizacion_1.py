import pickle

lista = ["Pedro","Ana","Maria","Isabel"]

fichero = open("lista","wb") #escritura binaria

pickle.dump(lista, fichero)#Volcado

fichero.close()

del (fichero)