class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Color: {self.color}\n"\
            f"Cantidad Ruedas: {self.ruedas}\n"

class Carro(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindraje):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    
    def __str__(self):
        return super().__str__() + f"Vehiculo: {self.velocidad}\n"\
            f"Cilindraje: {self.cilindraje}\n"

class Camioneta(Carro):
    def __init__(self, color, ruedas, velocidad, cilindraje, carga):
        super().__init__(color, ruedas, velocidad, cilindraje)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + f"Carga: {self.carga}\n"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + f"Tipo: {self.tipo}\n"

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindraje):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    
    def __str__(self):
        return super().__str__() + f"Velocidad: {self.velocidad}\n"\
            f"Cilindraje: {self.cilindraje}\n"

carro = Carro("Negro", 4, "130 km/h", "cc")
#print(str(carro))

bicicleta = Bicicleta("Blanca", 2, "Deportiva")
#print(str(bicicleta))

camion = Camioneta("Azul", 4, "100 km/h", "dd", "1000 kg")
#print(str(camion))

moto = Motocicleta("Verde", 2, "Deportiva", "200 km/h", "dd")
#print(str(moto))

def catalogar(vehiculos, ruedas =  None):
    if ruedas != None:
        contador = 0
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                contador += 1
            print(f"\nSe han encontrado {contador} con {ruedas} ruedas")
    for vehiculo in vehiculos:
        if ruedas == None:
            print(type(vehiculo).__name__, vehiculo)
        else:
            if vehiculo.ruedas == ruedas:
                print(type(vehiculo).__name__, vehiculo)

vehiculos = [carro, bicicleta, camion, moto]

catalogar(vehiculos, 4)