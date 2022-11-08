saldo = 1000

while True:
    print("\t::Menu::")
    print("\n1. Ingresar dinero ")
    print("2. Retirar Dinero")
    print("3. Mostrar dinero")
    print("4. Salir")
    opcion = int(input("Digite una opcion: "))
    if opcion == 1:
        ingreso = float(input("Cantidad a ingresar: "))
        print(f"Ingreso: {ingreso}")
        saldo +=  ingreso
    elif opcion == 2:
        retiro = float(input("Cantidad a retirar: "))
        if retiro > saldo:
            print("Saldo insuficiente")
        else:
            print(f"Se retiro: {retiro}")
            saldo -= retiro
    elif opcion == 3:
        print(f"Dinero disponible: {saldo}")
    elif opcion == 4:
        print("BYE")
        break
    else:
        print("Opcion incorrecta")
        break
    print()