
clientes = {}

def agregar(nombre,dni):
    if nombre not in clientes:
        clientes[nombre] = dni
        print("Cliente Agregado")
    else:
        print("Cliente Existente")

def mostar(clientes):
    for clave,valor in clientes.items():
        print(f"Nombre: {clave} Dni: {valor}")

def mostrar_dni(clientes,dni):
    for clave,valor in clientes.items():
        if dni == valor:
            print(f"Nombre: {clave} Dni: {valor}")

def eliminar(clientes,dni):
    if nombre in clientes:
        del(clientes[nombre])
        print("Contacto Eliminado")
    else:
        print("Contacto No Existe")


while True:
    print("\t::Menu::")
    print(" 1. Agregar Cliente")
    print(" 2. Mostrar Cliente")
    print(" 3. Mostrar Cliente por dni")
    print(" 4. Eliminar Cliente")
    print(" 5. Salir")
    opcion = int(input("Digite una opcion: "))
    print()

    if opcion == 1:
        nombre = input("Digite el nombre: ")
        dni = input("Digite el dni: ")
        agregar(nombre,dni)
        print()
    elif opcion == 2:
        mostar(clientes)
        print()
    elif opcion == 3:
        dni = input("Ingrese el dni del cliente: ")
        mostrar_dni(clientes,dni)
        print()
    elif opcion == 4:
        nombre = input("Introduzca el nombre del cliente a eliminar: ")
        eliminar(clientes,nombre)
        print()
    elif opcion == 5:
        print("bye")
        break
    else:
        print("Error")
        break
