from random import randint

numero = int(input("Digite un numero: "))
aleatorio = randint(0,100)

contador = 0
while numero != aleatorio:
    contador += 1
    if aleatorio > numero:
        print("Numero es mayor")
    else:
        print("Numero es menor")
    numero = int(input("Digite un numero: "))
print("Ganaste")
