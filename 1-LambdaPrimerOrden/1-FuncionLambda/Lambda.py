"""
Sintaxis: lambda argumentos: expresion
Utilizadas normalmente para funciones que se utilizan una sola vez, como argumentos de otras funciones, SIN NOMBRE.
Creando funciones en una sola linea en lugar de varias lineas.
Usada cuando usa funcion sera inecesaria o excesiva.
"""
#Lambda para sumar dos numeros
suma = lambda x, y: x + y

#Funcion Normal
def sumar(x, y):
    return x + y

print(suma(5, 3))  
print(sumar(5, 3))  

#2 Ejemplo
lista = [('1-Persona', 1.3), 
         ('2-Persona', 2.5), 
         ('3-Persona', 3.6),
         ('4-Persona', 3.2)]

def mostrarNumero(lista):
    return [x[1] for x in lista]

mostrarNumeros = lambda lista : [x[1] for x in lista]
print(mostrarNumeros(lista))
print(mostrarNumero(lista))