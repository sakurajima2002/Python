
""" def doblar_valor(numero):
    numero *= 2
    print(numero)

n = 5
doblar_valor(n) #Argumento por valor

print(n) """

""" def doblar_valor(numero):
    return numero*2

n = 5
n = doblar_valor(n)
print(n) """

#Argumentos por referencia

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

n = [5,10,15,20]
doblar_valores(n)#[:] para pasar argumentos por valor

print(n)