#Ejemplo de orden superior con funciones lambda
listaNotas = [('1-Persona', 1.3), 
         ('2-Persona', 2.5), 
         ('3-Persona', 3.6),
         ('4-Persona', 3.2)]

def mostrarNumero(lista):
    return lista[1]

print("Lista original, con funcion:")
lista_ordenada = sorted(listaNotas, key=mostrarNumero, reverse=True)
print(lista_ordenada)

print("Lista ordenada con funcion lambda:")
lista_ordenada_lambda = sorted(listaNotas, key= lambda lista: lista[1], reverse=True)
print(lista_ordenada)