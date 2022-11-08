
""" try:
    num = int(input("Ingrese un numero: "))
    print(f"9 / {num} y al dividirlo da {9/num}")
except Exception as e:
    print("Ocurrio el siguiente error",type(e).__name__) """

while True:
    try:
        num = int(input("Ingrese un numero: "))
        print(f"9 / {num} y al dividirlo da {9/num}")
        break
    except ValueError:
        print("No se puede dividir 9 entre texto")
    except ZeroDivisionError:
        print("No se puede dividir 9 entre 0")
    except Exception as error:
        print("Ocurrio el siguiente error",type(error).__name__)
