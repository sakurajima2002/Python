
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args,**kwargs): # *args para recibir un numero indeterminado de parametros
        print("Vamos a Realizar un Calculo")
        funcion_parametro(*args,**kwargs) # **kawargs argumentos con clave valor
        print("Hemos Terminado el Calculo")
    return funcion_interior

@funcion_decoradora
def suma(num1, num2 , num3):
    print(num1 + num2 + num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))

suma(7,5,8)
resta(12,10)
potencia(base=5,exponente=3)
