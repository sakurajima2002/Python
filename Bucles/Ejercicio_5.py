
numero = int(input("Digite un numero: "))

while numero<0:
    print("Error")
    numero = int(input("Digite un numero: "))

factorial = 1
for i in range(1,numero+1):
    factorial  *= i

print(f"{numero} el factorial es {factorial}")
