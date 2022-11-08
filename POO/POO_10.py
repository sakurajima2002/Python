import copy

class Producto:
    def __init__(self, ref, nombre, precio, descripcion):
        self.ref = ref
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return f"Referencia: \t {self.ref}\n"\
        f"Nombre: \t {self.nombre}\n"\
        f"Precio:  \t {self.precio}\n"\
        f"Descripcion: \t {self.descripcion}\n"

class Combo(Producto):
    pass

class Alimento(Producto):
    marca = ""
    categoria = ""

    def __str__(self):
        return f"Referencia: \t {self.ref}\n"\
        f"Nombre: \t {self.nombre}\n"\
        f"Precio:  \t {self.precio}\n"\
        f"Descripcion: \t {self.descripcion}\n"\
        f"Marca:  \t {self.marca}\n"\
        f"Categoria:  \t {self.categoria}\n"

class Ropa(Producto):
    marca = ""
    categoria = ""
    talla = ""

    def __str__(self):
        return f"Referencia: \t {self.ref}\n"\
        f"Nombre: \t {self.nombre}\n"\
        f"Precio:  \t {self.precio}\n"\
        f"Descripcion: \t {self.descripcion}\n"\
        f"Marca:  \t {self.marca}\n"\
        f"Categoria:  \t {self.categoria}\n"\
        f"Talla:  \t {self.talla}\n"


combo1 = Combo('1','Combo 1',150,'Harina de maiz (1kg), Carne Res (2kg)')

harina = Alimento(1111, "Harina de Maiz", 50, "Harina Precocida")
harina.marca = "Mejor"
harina.categoria = "Comida"

pantalon1 = Ropa(1234, "Jean Hombre", 90, "Oversize")
pantalon1.marca = "Levis"
pantalon1.categoria = "Hombre"
pantalon1.talla = 28

productos = [combo1, harina]
productos.append(pantalon1)

for producto in productos:
    if (isinstance(producto,Combo)):
        print(producto.ref, producto.nombre)
    elif (isinstance(producto,Ropa)):
        print(producto.ref, producto.nombre , producto.talla)
    elif (isinstance(producto,Alimento)):
        print(producto.ref, producto.nombre , producto.marca)

def descuento(producto , rebaja):
    producto.precio = producto.precio - (producto.precio * (rebaja/100))
    return producto

pantalon_desc = descuento(pantalon1, 20)
copiapant = copy.copy(pantalon1)
copiapant.precio = 500
print(copiapant)
print(pantalon_desc)