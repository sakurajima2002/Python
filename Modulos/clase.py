class Vehiculos():

    def __init__(self,marca,modelo):#constructor
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def  arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Enmarcha: {self.enmarcha}")
        print(f"Frena: {self.frena}")
        print(f"Acelera: {self.acelera}")

class Furgoneta(Vehiculos):

    def carga(self , cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La Furgoneta esta cargada"
        else:
            return "La Furgoneta no esta cargada"

class Moto(Vehiculos): #Herencia
    hcaballido = ""

    def caballido(self):
        self.hcaballido = "Voy haciendo caballido"

    def estado(self): #Sobreescritura metodos
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Enmarcha: {self.enmarcha}")
        print(f"Frena: {self.frena}")
        print(f"Acelera: {self.acelera}")
        print(self.hcaballido)

class VehiculosElectricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
        self.cargando = False

    def cargarEnergia(self):
        self.cargando = True

    def estado(self):
        super().estado()
        print(f"Autonomia: {self.autonomia}")
        print(f"Cargando: {self.cargando}")

class BicicletaElectrica(VehiculosElectricos,Vehiculos):#herencia multiple
    pass
