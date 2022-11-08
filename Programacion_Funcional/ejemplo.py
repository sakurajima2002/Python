class Estudiante:
    def __init__(self, nombre, materia, nota, recuperacion=None, validacion=None):
        self.nombre = nombre
        self.materia = materia
        self.nota = nota
        self.recuperacion = recuperacion
        self.validacion = validacion
    
    def __str__(self):
        return f"El estudiante {self.nombre} de la materia {self.materia} tiene la nota de {self.nota}"

listaEstudiantes = [
    Estudiante("Juan", "Ciencias", 3.4),
    Estudiante("Santiago", "Matematicas", 2.9, True, "B"),
    Estudiante("Camilo", "Informatica", 2.2),
    Estudiante("Carlos", "Ciencias", 4.5),
    Estudiante("Samuel", "Ciencias", 2.5, True, "E"),
    Estudiante("Emanuel", "Matematicas", 4.5),
    Estudiante("Andres", "Matematicas", 3.5),
    Estudiante("Fernando", "Ciencias", 2.9, True, "Bj"),
    Estudiante("Leonel", "Informatoca", 3.7),
]

estudiantesReprobados = filter(lambda estudiante:estudiante.nota >= 3.0 and estudiante.nota <= 5.0, listaEstudiantes)
estudiantesAprobados = filter(lambda estudiante:estudiante.nota >= 0.0 and estudiante.nota <= 2.9, listaEstudiantes)

print("\t:::Estudiantes Aprobados:::")
for estudiantes in estudiantesAprobados:
    print(estudiantes)

print("\n\t:::Estudiantes Reprobados:::")
for estudiantes in estudiantesReprobados:
    print(estudiantes)

def recuperacionEstudiantes(estudiante):
    if estudiante.recuperacion:
        if estudiante.validacion == 'E' or estudiante.validacion == 'e':
            estudiante.nota += 1.0
        elif estudiante.validacion == 'B' or estudiante.validacion == 'b':
            estudiante.nota += 0.5
        elif estudiante.validacion == 'Bj' or estudiante.validacion == 'bj':
            estudiante.nota += 0.2
        else:
            estudiantes.nota += 0
    return estudiante

notasFinales = map(recuperacionEstudiantes, listaEstudiantes)

print("\n\t:::Notas despues de Recuperaciones:::")
for estudiante in notasFinales:
    print(estudiante)
