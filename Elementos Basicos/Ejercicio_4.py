#Hacer un programa para ingresar el radio de un circulo y
#se reporte su area y longitud de la circunferencia

from cmath import pi


radio = float(input("Digite el radio del circulo: "))

area = pi * radio**2
longitud = 2 * pi *radio


print(f"El area de la circunferencia es: {area:.2f}")
print(f"La longitud de la circunferencia es {longitud:.2f}")