#Hacer un programa que pida un caracter en indique si es vocal o no

letra = input("Digite una vocal: ").lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o'  or letra == 'u':
    print("Es una vocal")
else:
    print("No es una vocal")