class Torta():
    glaciado = False
    def __init__(self, sabor=None, color=None):
        self.sabor = sabor
        self.color = color
        if sabor is not None and color is not None:
            print(f"Torta Creada con sabor {self.sabor} y color {self.color}")
        else:
            print(f"Torta vainilla")
    def glaciados(self):
        self.glaciado = True

    def esta_glaciada(self):
        if self.glaciado:
            print("Torta no esta glaciada")
        else:
            print("Torta  glaciada")

torta = Torta("Fresa", "Blanca")
torta.esta_glaciada()
