class Video():
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

    def __str__(self):
        return f"Titulo: {self.titulo} \nDuracion: {self.duracion} \nLanzamiento: {self.lanzamiento}"

    def __len__(self):
        return self.duracion

    #Destructor
    def __del__(self):
        print(f"{self.titulo} Elimindo")

video_1 = Video("Pokemon",123,2002)
video_2 = Video("Dragon",143,2000)

print(str(video_1))
print("----------------------")
print(str(video_2))
print("----------------------")
print(len(video_1))
print(len(video_2))
print("----------------------")

