
def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{i} * {num} = {num*i}")

while True:
    print()
    opcion = input("Realizar tabla multiplicar de un numero (S/N): ")
    if opcion == 'S' or opcion == 's':
        numero = int(input("Digite el numero a multiplicar: "))
        tabla_multiplicar(numero)
    else:
        print("Bye")
        break