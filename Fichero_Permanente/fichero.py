import pickle

class Persona():
    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f"Persona creada: {self.nombre}")

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersona:
    personas = []

    def __init__(self):
        listaPersonas = open("FicheroExterno","ab+") #agregar
        listaPersonas.seek(0)
        try:
            self.personas = pickle.load(listaPersonas)
            print("Se cargaron {} personas".format(len(self.personas)))

        except:
            print("El fichero esta vacio")

        finally:
            listaPersonas.close()
            del (listaPersonas)

    def agregarPersona(self, persona):
        self.personas.append(persona)
        self.guardarPersona()

    def mostrarPersona(self):
        for i in self.personas:
            print(i)

    def guardarPersona(self):
        listaPersonas = open("FicheroExterno","wb")
        pickle.dump(self.personas,listaPersonas)
        del (listaPersonas)

    def mostarInfo(self):
        print("\n\t::La imformacion del Archivo::")
        for i in self.personas:
            print(i)

miLista = ListaPersona()

persona1 = Persona("Ana","Masculino","49")
miLista.agregarPersona(persona1)
miLista.mostarInfo()





