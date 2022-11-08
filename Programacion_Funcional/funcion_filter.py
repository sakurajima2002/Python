
class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} trabaja como {self.cargo} tiene un salario {self.salario} $"

listaEmpleado =[
    Empleado("Juan","Director",90000),
    Empleado("Ana","Gerente",100000),
    Empleado("Carlos","Finanzas",2000),
    Empleado("Antonio","Contador",8000),
    Empleado("Pedro","Selador",70000),
]

salarios_altos = filter(lambda empleado:empleado.salario>20000,listaEmpleado)

for empleado_salario in salarios_altos:
    print(empleado_salario)