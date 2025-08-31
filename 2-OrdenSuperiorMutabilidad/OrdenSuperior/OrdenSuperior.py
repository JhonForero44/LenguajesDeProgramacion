"""
Una funcion se denomina de orden superior si este contiene otras fucniones como parametros de 
entrada o si devuelve una funcion como salida, es decir, las funciones que operan con otras 
funcion se conoce como Funciones de Orden Superior.
"""

#1 -> Ejemplo, raiz cuadradad y potenciaCuadrado de una funcion
def operacion(funcion, valor):
    return funcion(valor)

def raiz_cuadrada(x):
    return x**(1/2)

def potenciaCuadrado(x):
    return x**2

raizCuadrado = operacion(raiz_cuadrada, 9)
print(raizCuadrado)
potencia = operacion(potenciaCuadrado, 3)
print(potencia)

#Filter -> Filtra los elementos de una lista que cumplen con una condicion
#Estructura -> filter(funcion, iterable)
#Lista
integer = [1,2,3,4,5,6,7,8,9,10,11,12]
#Funcion numeros pares, lambda=funcion, integer=integer
even = list(filter(lambda x: x%2==0, integer))
print(even)

#Map -> Aplica una funcion especifica a cada elemento de una lista. El objeto se envia a la funcion como parametro.
#Estructura -> map(funcion, iterable)
#Funcion cubo, lambda=funcion integer=integer
cubo = list(map(lambda x: x**3, integer))
print(cubo)

#Reduce -> Aplica una funcion a una secuencia de elementos y los reduce a un unico valor.
#Estructura -> reduce(funcion, iterable)
from functools import reduce
#Funcion suma, lambda=funcion integer=integer
suma = reduce(lambda x, y: x+y, integer)
print(suma)