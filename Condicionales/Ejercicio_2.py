#Hacer un programa que pida tres numeros y determine el mayor

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

if num1 > num2 and num1 > num3:
    print(f"Numero mayor es {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Numero mayor es {num2}")
elif num3 > num1 and num3 > num2:
    print(f"Numero mayor es {num3}")
else:
    print("Son iguals")