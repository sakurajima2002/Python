a = int(input("Numero de inicio: "))
b = int(input("Numero de Final: "))

suma = 0

for i in range(a,b+1):
    if i%2==0:
        suma += i

print(f"La suma es: {suma}")