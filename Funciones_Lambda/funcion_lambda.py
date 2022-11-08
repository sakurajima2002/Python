""" def area_triangulo(base,altura):
    return (base*altura)/2

triangulo1 = area_triangulo(9,6)
triangulo2 = area_triangulo(8,2)

print(triangulo1)
print(triangulo2) """

""" area_triangulo = lambda base,altura:(base*altura)/2
print(area_triangulo(7,5)) """

""" al_cubo = lambda numero:pow(numero,3)
#al_cubo = lambda numero:numero**3

print(al_cubo(13)) """

destacar_valor = lambda comision:f"¡{comision}! $"

comision = 10000

print(destacar_valor(comision))