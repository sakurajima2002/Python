
cadena1 = input("Digite una palabra: ")
cadena2 = input("Digite otra palabra: ")

if len(cadena1) == len(cadena2):
    print("Son iguales")
elif len(cadena1) > len(cadena2):
    print(cadena1)
else:
    print(cadena2)