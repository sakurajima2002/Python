#Hacer un programa que intercambie el valor de dos variables

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

num1 , num2 = num2 , num1

print(f"Valor del numero 1 {num1}")
print(f"Valor del numero 2 {num2}")
