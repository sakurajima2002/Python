import re

nombre1 = "juan Laverde"
nombre2 = "Sebastian Gonzalez"
nombre3 = "JuanSe Laverde"
cadena1 = "54656654665"
cadena2 = "a6734384639"
codigo1 = "jashjasalsalsalshajshasa71alsalsalsalshasfswu"

if re.match(".uan",nombre1,re.IGNORECASE):
    print("Nombre Encontrado")
else:
    print("Nombre No Encontrado")

if re.match("\d",cadena1):
    print("Numero Encontrado")
else:
    print("Numero No Encontrado")

if re.search("Laverde",nombre1,re.IGNORECASE):
    print("Apellido Encontrado")
else:
    print("Apellido No Encontrado")

if re.search("71",codigo1):
    print("Codigo Encontrado")
else:
    print("Codigo No Encontrado")