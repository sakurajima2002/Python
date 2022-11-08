
while True:

    try:

        numero = int(input("Digite un numero: "))

        print(f"La suma es: {numero+10}")
        break

    except:
        print("Ha ocurrrido un error")

    else:
        print("Programa Terminado correctamente")
        break

    finally:
        print("Interaccion finalizada")

print("Programa Terminado")