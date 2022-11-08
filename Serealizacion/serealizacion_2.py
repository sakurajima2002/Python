import pickle

fichero = open("lista","rb")#leer binario

lista = pickle.load(fichero)#cargar

print(lista)
