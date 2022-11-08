import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Cuadrante I")
        elif self.x < 0 and self.y > 0:
            print("Cuadrante II")
        elif self.x < 0 and self.y < 0:
            print("Cuadrante III")
        elif self.x > 0 and self.y < 0:
            print("Cuadrante IV")
        elif self.x == 0 or self.y == 0:
            print("Uno es Cero")
        else:
            print("Ambos son 0")

    def vector(self, punto):
        print(f"El vector que une los puntos {self} y {punto} = ({punto.x - self.x},{punto.y - self.y})")

    def distancia(self, punto):
        resultado = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        print(f"La distancia entre los puntos {self} y {punto} = {resultado}")

class Rectagulo:
    def __init__(self, inicial=Punto(0,0), final=Punto(0,0)):
        self.inicial = inicial
        self.final = final
        self.base = abs(self.final.x - self.inicial.x)
        self.altura = abs(self.final.y - self.inicial.y)
        self.area = self.base * self.altura

    def mostar_base(self):
        print(f"La base es {self.base}")

    def mostar_altura(self):
        print(f"La altura es {self.altura}")

    def mostar_area(self):
        print(f"El area es {self.area}")

p1 = Punto(-8,4)
print(str(p1))
p1.cuadrante()

p2 = Punto(5,8)
p3 = Punto(-8,4)
p2.vector(p3)
p2.distancia(p3)

print("---------------------------")

p4 = Punto(6,8)
p5 = Punto(10,4)

rec = Rectagulo(p4,p5)
rec.mostar_base()
rec.mostar_altura()
rec.mostar_area()
