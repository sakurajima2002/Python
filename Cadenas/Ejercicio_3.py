
cadena = input("Digite una cadena: ")

cadena = cadena.replace(" ","")

cadena2 = cadena[::-1]

print(cadena2)

if cadena.lower() == cadena2.lower():
    print("La Cadena es palindromo")
else:
    print("La cadena no es palindromo")