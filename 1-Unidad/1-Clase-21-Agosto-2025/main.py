from calculadora import *

def division (a,b):
    if b != 0:
        return a / b

if __name__ == "__main__":
    
    operacion = input("Ingrese la operación (+, -, *, /): ")
    funcion = None
    
    operador1 = int (input("Ingrese el primer operando: "))
    operador2 = int (input("Ingrese el segundo operando: "))
     
    #Version 1, Funcion Lambda
    #Version 1: Asignamos la funcion a la rariable de acuerdo a la operación con una función lambda
    
    if operacion == "+":
        funcion = lambda a, b : a + b #Funcion sin nombre, que recibe dos parametros y los suma
    elif operacion == "-":
        funcion = lambda a, b : a - b #Funcion sin nombre, que recibe dos parametros y los resta
    elif operacion == "*":
        funcion = lambda a, b : a * b #Funcion sin nombre, que recibe dos parametros y los resta
    elif operacion == "/":
        funcion = division
        
    resultado = funcion(operador1, operador2)
    #Devuelve la funcion: calculadora_1(operacion)
    resultado_2 = calculadora_1(operacion)(operador1, operador2)
    
    #Version 3
    operaciones = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": division
    }

    resultado_3 = operaciones[operacion](operador1, operador2)
        
    print(f"El resultado es: {resultado}")
    print(f"El resultado de la version 2 es: {resultado_2}")
    print(f"El resultado de la version 3 es: {resultado_3}")
    """
    print(f"El resultado de {operacion} entre {operador1} y {operador2} es: {resultado(operador1, operador2)}")
    """
    
#Estos temas estan conectados en PrimerOrden y Anonimas