#Calculadore basica

from __future__ import division


num1 = float(input("Digite un numero: "))
num2 = float(input("Digite un numero: "))
print("Suma (S/s)")
print("Multiplicacion (M/m)")
print("Division (D/d)")
print("Resta (R/r)")
opcion = input("Digite una opcion: ")

if opcion == 'S' or opcion == 's':
    suma = num1 + num2
    print(f"{num1} + {num2} = {suma}")
elif opcion == 'R' or opcion == 'r':
    resta = num1 - num2
    print(f"{num1:} - {num2} = {resta}")
elif opcion == 'M' or opcion == 'm':
    multplicacion = num1 * num2
    print(f"{num1} * {num2} = {multplicacion:.2f}")
elif opcion == 'D' or opcion == 'd':
    division = num1 / num2
    print(f"{num1} / {num2} = {division:.2f}")
else:
    print("Opcion invalida")