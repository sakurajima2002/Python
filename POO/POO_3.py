class Persona():
    def __init__(self,nombre,edad,recidencia):
        self.nombre = nombre
        self.edad = edad
        self.recidencia = recidencia

    def descripcion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Residencia: {self.recidencia}")

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre,edad,recidencia):
        super().__init__(nombre,edad,recidencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario}")
        print(f"Antiguedad: {self.antiguedad}")

empleado = Empleado(1500,1,"Juan",19,"Colombia")
empleado.descripcion()
print(isinstance(empleado,Persona))