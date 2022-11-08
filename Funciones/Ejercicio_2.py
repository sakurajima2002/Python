def dibujar(ancho,alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ",end="")
        print()


ancho = int(input("Digite la anchura: "))
alto = int(input("Digite la atura altura: "))

print()
dibujar(ancho,alto)
