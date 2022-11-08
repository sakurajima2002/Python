import re

cadena = "Vamos a aprender expresiones regulares en Python . Python es un lenguaje de sintaxis sencilla"

textoBuscar = "Python"

""" textoEncontrado = re.search(textoBuscar,cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span()) """

print(len(re.findall(textoBuscar,cadena)))