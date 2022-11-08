class Producto:
    def __init__(self,cod,nombre,categoria,precio):
        self.cod = cod
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f'{self.nombre} - {self.precio}'

class Negocio:
    def __init__(self,productos=[]):
        self.productos = productos

    def mostrar_producto(self, cod=None):
        for producto in self.productos:
            if producto.cod == cod:
                print(producto)
                return
        print('Producto not found')

    def borrar_producto(self, cod=None):
        for i , producto in enumerate(self.productos):
            if producto.cod == cod:
                del(self.productos[i])
                print(str(producto),'-> Eliminado')
                return
        print('Producto Not Fount')

producto1 = Producto('1','Pera','fruta',23)
producto2 = Producto('2','Manzana','fruta',33)

negocio = Negocio(productos=[producto1,producto2])

negocio.mostrar_producto('1')
negocio.mostrar_producto('2')
negocio.borrar_producto('1')
negocio.mostrar_producto('1')