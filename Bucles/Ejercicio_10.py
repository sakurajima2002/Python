
cadena = input("Digite una frase: ")
lista = []

for i in cadena:
    if i not in lista:
        lista.append(i)
print(f"Lista caracteres sin repetir: \n{lista}")