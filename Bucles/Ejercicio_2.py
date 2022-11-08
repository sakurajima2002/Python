
lista = list(range(1,11))
for i in lista:
    print(i,end="-")

numero = int(input("\nDigite el numero por el que quiere multiplicar: "))

for mult,i in enumerate(lista):
    mult = i * numero
    print(mult,end="-")