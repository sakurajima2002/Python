
class Area:

    """ Esta clase calcula el area de
    diferentes figuras geometricas"""

    def areaCuadrado(lado):

        """ Calcula el area de un cuadrdo
        elevando al cuadrado el lado pasado
        por parametro"""

        return "El area del cuadrado es: "+str(lado*lado)

    def areaTriangulo(base,altura):

        """ Calcula el area de un triangulo
        utilizando los parametros base y altura"""

        return "El area del triangulo es: "+str((base * altura)/2)


#print(Area.areaCuadrado.__doc__) #imprime documentacion
#help(Area.areaCuadrado)
help(Area)
