"""

Hacer un programa que simule un cajero automatico con un
saldo inicial de $1000 y tendra el siguiente menu de opciones:

1.Ingresar dinero
2.Retirar dinero
3.Mostrar dinero
4.Salir

"""

saldo = 1000

print("\n\t::Menu::")
print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero de la cuenta")
print("4. Salir")
opcion = int(input("Digite una opcion: "))
print()

if opcion == 1:
    aumento = float(input("Cantidad de dinero que sea ingresar:"))
    saldo += aumento
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 2:
    descuento = float(input("Digite la cantidad que desea retitar: "))
    if descuento > saldo:
        print("Error saldo insuficiente")
    else:
        saldo -= descuento
        print(f"Saldo actual : {saldo}")
elif opcion == 3:
    print(f"Saldo: {saldo}")
elif opcion == 4:
    print("Bye")
else:
    print("Opcion incorrecta")