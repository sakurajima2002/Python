
class Coche():

    def __init__(self): #Constructor
        #Propiedades
        self.__largoChasis = 250
        self.__anchorChasis = 120
        self.__ruedas = 4 #__variable -> para encapsular
        self.__enmarcha = False

    #Comportamientos
    def arrancar(self,arrancamos): #self == this
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo == False):
            return "No podemos arrancar"
        else:
            return "El coche esta parado"

    def estado(self):
        print(f"El coche tiene: {self.__ruedas} ruedas")
        print(f"El largo del coche es: {self.__largoChasis}")
        print(f"El ancho del coche es: {self.__anchorChasis}")

    def __chequeo_interno(self): #Metodo encapsulado
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False


print("\t::Coche 1::")
miCoche = Coche() #Instanciar clase
miCoche2 = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("\n\t::Coche 2::")

print(miCoche2.arrancar(False))
miCoche2.estado()



