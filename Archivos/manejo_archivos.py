from io import open

###Modo escritura
# archivo_texto = open("archivo.txt","w")
# frase = "Estupendo dia para estudiar Python\nDomingo"
# archivo_texto.write(frase)
# archivo_texto.close()

###Modo lectura
archivo_texto = open("archivo.txt","r")
texto1 = archivo_texto.read()
texto2 = archivo_texto.readlines()
archivo_texto.close()
print(texto1)
print(texto2)

# ###Modo agregar
# archivo_texto = open("archivo.txt","a")
# archivo_texto.write("\nSimpre es una buena ocasion para estudiar Python")
# archivo_texto.close()
