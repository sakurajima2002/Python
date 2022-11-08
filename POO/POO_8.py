class Videojuego:
    def __init__(self, titulo, genero, lanzamiento):
        self.titulo = titulo
        self.genero = genero
        self.lanzamiento = lanzamiento
        print('se creo el videojuego: ',self.titulo)

    def __str__(self):
        return f"{self.titulo}:{self.lanzamiento}"

class Catalogo:
    videjuegos = []
    def __init__(self, videojuegos=[]):
        self.videojuegos = videojuegos

    def agregar(self, videojuego):
        self.videojuegos.append(videojuego)

    def mostar(self):
        for videojuego in self.videojuegos:
            print(videojuego)

v1 = Videojuego('the last', 'acción', 2002)
v2 = Videojuego('galaxis', 'ciencia', 2019)
v3 = Videojuego('likes', 'romance', 2012)

juegos = Catalogo([v1, v2, v3])

v4 = Videojuego('music', 'musica', 2013)

juegos.agregar(v4)
juegos.mostar()

