
def pesos_dolar(pesos):
    cantidad = pesos / 4083.07
    print(f"${pesos} pesos equivale a ${cantidad:.2f} dolares")

def dolar_pesos(dolares):
    cantidad = dolares * 4083.07
    print(f"${dolares} dolares equivale a ${cantidad:.2f} pesos")

while True:
    print("\t::Menu::")
    print("1. Pasar de Pesos a Dolares")
    print("2. Pasar de Dolares a Pesos")
    print("3. Salir")
    opcion = int(input("Digite una opcion: "))

    if opcion == 1:
        pesos = float(input("Digite la cantidad de pesos a cambiar: "))
        pesos_dolar(pesos)
    elif opcion == 2:
        dolares = float(input("Digite la cantidad de dolares a cambiar: "))
        dolar_pesos(dolares)
    elif opcion == 3:
        print("BYE")
        break
    else:
        print("Opcion Fuera de Rango")
        break