#Argumentos Indeterminados

""" def argumentar(*args):
    for elemento in args:
        print(elemento)

argumentar("Juan",[1,2,3,4],5) """

""" def nombrar(**kwargs):
    for clave in kwargs:
        print(clave,":",kwargs[clave])

nombrar(nombre="Juan", id=5, notas=[50,45,35]) """

def super_nominacion(*args,**kwargs):
    suma = 0
    for i in args:
        suma += i
    print(f"La promedio indeterminado es: {suma/len(args)}")
    for clave in kwargs:
        print(clave,":",kwargs[clave])

super_nominacion(10, 10, 10, 20, 3, 4,
                 id=5, nombre="Juan",
                 edad=19, notas=[50,30,45])