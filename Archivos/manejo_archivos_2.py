from io import open

archive = open("archivo.txt","r+") # lectura y escritura

#archive.seek(len(archive.read())/2)
#archive.seek(len(archive.readline()))
#print(archive.read())

#archive.write("comienzo texto ")
#print(archive.readlines())

line = archive.readlines()
line[1] = "Esta linea ha sido incluida desde el exterior\n"
archive.seek(0)
archive.writelines(line)
archive.close()