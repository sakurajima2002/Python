
def dividir():
    while True:
        try:
            num1 = float(input("Digite un numero: "))
            num2 = float(input("Digite un numero: "))
            resultado = num1 / num2
            print(f"El resultado es: {resultado:.2f}")

        except ValueError:
            print("Error -> Digite correctmente los valores numericos")

        except ZeroDivisionError:
            print("Error -> No se puede dividir en cero")

        else:
            break

dividir()
