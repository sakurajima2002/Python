
#Modo escritura "w"
with open(r'/home/zoro/Documentos/Python/output.txt','w') as f:
    f.write("Escritura Ficheros")
    f.write("\nOtra linea")
    f.write(" Y misma linea")

#Modo lectura "r"
""" with open(r'/home/zoro/Documentos/Python/output.txt','r') as f:
    print(f.read()) """

#Leer linea por linea
""" with open(r'/home/zoro/Documentos/Python/output.txt','r') as f:
    data = f.readlines()
    print(data) """

""" with open(r'/home/zoro/Documentos/Python/output.txt','r') as f:
    for linea in f:
        print(linea) """

#Leer Palabra por Palabra
""" with open(r'/home/zoro/Documentos/Python/output.txt','r') as f:
    for linea in f:
        palabras = linea.split()
        print(palabras , type(palabras)) """

palabras = list()
with open(r'/home/zoro/Documentos/Python/output.txt','r') as f:
    for linea in f:
        termino_1 = linea.split()
        for t in termino_1:
            palabras.append(t)
    print(palabras, type(palabras))