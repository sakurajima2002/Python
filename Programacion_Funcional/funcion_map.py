class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} trabaja como {self.cargo} tiene un salario {self.salario} $"

listaEmpleado =[
    Empleado("Juan","Director",9000),
    Empleado("Ana","Gerente",10000),
    Empleado("Carlos","Finanzas",2000),
    Empleado("Antonio","Contador",8000),
    Empleado("Pedro","Selador",7000),
]

def calculo_comision(empleado):
    if empleado.salario<=8000:
        empleado.salario = empleado.salario * 1.03
    return empleado

listaEmpleadosComision = map(calculo_comision,listaEmpleado)

for empleado in listaEmpleadosComision:
    print(empleado)
