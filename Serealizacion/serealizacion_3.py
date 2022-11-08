import pickle

class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.arranque = False
        self.frena = False

    def encender(self):
        self.encendido = True

    def arrancar(self):
        self.arranque = True

    def frenando(self):
        self.frena = True

    def mostrar(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Encendido: {self.encendido}")
        print(f"Arranque: {self.arranque}")
        print(f"Frenando: {self.frena}")

coche1 = Vehiculos("Mazda","MX5")
coche2 = Vehiculos("Audi","ST5")
coche3 = Vehiculos("Pegout","09O")

coches = [coche1,coche2,coche3]

fichero = open("LosCoches","wb")

pickle.dump(coches,fichero)

fichero.close()

del (fichero)

fichero_Apertura = open("LosCoches","rb")

misCoches = pickle.load(fichero_Apertura)

fichero_Apertura.close()

for i in misCoches:
    print(i.mostrar())
    print("\n")
