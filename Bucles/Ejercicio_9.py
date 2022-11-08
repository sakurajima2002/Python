
frase = input("Digite una frase:")
frase2 = ""

for i in frase:
    if i!=" ":
        frase2 += i
frase = frase2
print(f"\nFrase Final: {frase}")
print(f"Cantidad de caracteres: {len(frase)}")