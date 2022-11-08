
def factorial(num):
    if num>0:
        resultado = num * factorial(num-1)
    else:
        resultado = 1

    return resultado


numero = int(input("Digite un numero: "))

while numero<0:
    print("Error debe ser un numero positivo")
    numero = int(input("Digite un numero: "))
print(factorial(numero))
