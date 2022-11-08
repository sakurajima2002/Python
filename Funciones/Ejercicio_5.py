
def digitos(num):
    if num == 0:
        resultado = 0
    else:
        resultado = digitos(int(num/10)) + (num%10)
    return resultado

numero = int(input("Digite un numero: "))

print(digitos(numero))