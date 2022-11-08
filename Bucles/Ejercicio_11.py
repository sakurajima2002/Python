contactos = {}

while True:
    print("\t::Menu::")
    print(" 1. Nuevo Contacto")
    print(" 2. Borrar Contacto")
    print(" 3. Ver Contacto")
    print(" 4. Salir")
    opcion = int(input("Digite una opcion: "))
    print()
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ")
        numero = int(input("Digite el numero del contacto: "))

        if nombre not in contactos:
            contactos[nombre] = numero
            print("Contacto Agregado")
        else:
            print("Contacto Existente")

    elif opcion == 2:
        nombre = input("Digite el nombre del contacto: ")
        if nombre in contactos:
            del(contactos[nombre])
            print("Contacto Eliminado")
        else:
            print("Contacto No Existe")

    elif opcion == 3:
        print("Contactos Existentes")
        for clave,valor in contactos.items():
            print(f"Nombre: {clave}, Telefono: {valor}")

    elif opcion == 4:
        print("BYE")
        break

    else:
        print("Opcion Incorrecta")
        break

    print()