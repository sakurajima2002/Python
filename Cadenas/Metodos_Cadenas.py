
#cadena = "Hola mundo".upper() #convierte caracteres en mayusscula
#cadena = "Hola mundo".lower() #convierte caracteres en minuscula
#cadena = "hola mundo".capitalize() #Pone primer letra en mayuscula
#cadena = "hola mundo".title()#convierte en mayuscula la primer letra de cada palabra
#cadena = "Hola mundo".count('o') #cuanta determinado caracter o palabra
#cadena = "Hola mundo".find('mundo') #busca en que indice se encuentra la concidencia
#cadena = "10000".isdigit() #Determina si la cadena es de caracteres numericos
#cadena = "AsTq".isalpha() #determina si solo ahi caracteres alfabeticos
#cadena = "ATqx".isalnum() #Determina si en nuestra cadena ahi caracteres alfanumericos
#cadena = "hola mundo".islower() #Determina si la cadena esta en minuscula
#cadena = "Toda".isupper() #Determina si todo esta en mayuscula
#cadena = "Hola Mundo".istitle() #Detrrmina si cada palabra inicia en mayuscula
#cadena = "    ".isspace() #Determina si la cadena esta conformada solamnete por espacios
#cadena = "hola mundo".startswith('h') #Dtermina si la cadena comienza con cierto caracter o palabra
#cadena = "Hola Mundo".endswith('o') #Dtermina si la cadena termina con cierto caracter o palabra
#cadena = "Hola-Mundo".split('-') #separa los elementos que los diferencie un espacio en una lista
#cadena = ",".join("Hola mundo")
#cadena = "....hola...".strip('.') #Elimina espacios o simbolos
cadena = "Hola mundo".replace('Hola','HOLA')

print(cadena)