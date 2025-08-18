"""
Funcion anidad dentro de otra funcion.
Son funciones que:
    1->Reciben una funcion como argumento
    2->Devuelven una funcion como resultado
"""

#Ejemplo con el primer caso, imprimir una palabra en alto o bajo.
def imprimir_mayuscula(texto):
    return texto.upper()

def imprimir_minuscula(texto):
    return texto.lower()    

def imprimir(funcion):
    texto = funcion("Hola Mundo")
    return texto

print(imprimir(imprimir_mayuscula))
print(imprimir(imprimir_minuscula))

#Ejemplo con el segundo caso, devolver una funcion.
def divisor(x):
    def dividiendo(y):
        return y / x
    #divisor retorna la función dividiendo
    return dividiendo

#Nueva funcion a partir de divisor con el numero 2
dividir_por_2 = divisor(2)

#Cuando se llame dividir_por_2(10), pasa 10, por lo cual se haria la operacion 10 / 2
print(dividir_por_2(10))
