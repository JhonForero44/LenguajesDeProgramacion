#Importar libreria
from functools import reduce

# 1-> Genere de forma perezosa los números hasta 100 millones.
def generador():
    for i in range(100000000):
        yield i+1

numeros = generador()

#Consumidor
listaNumeros = []
for i in range(300):
    nuevoNumero = next(numeros)
    listaNumeros.append(nuevoNumero)

print(f"1 -> Lista nuevo Numeros: {listaNumeros}")

# 2-> Filtre solo aquellos que sean múltiplos de 4 y además terminan en 6.
print()
listaNumerosFiltradoCuatroSeis = list(filter(lambda x: (x % 4 == 0) and (str(x).endswith("6")), listaNumeros))
print(f"2 -> Lista Filtrado Cuatro-Seis: {listaNumerosFiltradoCuatroSeis}")

# 3-> Transforme cada número filtrado elevándolo al cubo.
print()
listaNumerosFiltradoCuatroSeisTransformadoCubo = list(map(lambda x: x ** 3, listaNumeros))
print(f"3 -> Lista Filtrado Cuatro-Seis - Transformado Cubo: {listaNumerosFiltradoCuatroSeisTransformadoCubo}")

# 4-> Consuma únicamente los primeros 30 resultados procesados.
print()
listaNumerosFiltradoCuatroSeisTransformadoCuboProcesados = list(map(lambda x: x, listaNumerosFiltradoCuatroSeisTransformadoCubo[:30]))
print(f"4 -> Lista Filtrado Cuatro-Seis - Transformado Cubo - Primero Resultados: {listaNumerosFiltradoCuatroSeisTransformadoCuboProcesados}")

# 5> Calcule el promedio de esos resultados.
print()
cantidadDatos = len(listaNumerosFiltradoCuatroSeisTransformadoCuboProcesados)
listaNumerosFiltradoCuatroSeisTransformadoCuboProcesadosReducido = reduce(lambda x,y : x+ y, listaNumerosFiltradoCuatroSeisTransformadoCuboProcesados)
print(f"5 -> Lista Filtrado Cuatro-Seis - Transformado Cubo - Primero Resultados - Reducido: {listaNumerosFiltradoCuatroSeisTransformadoCuboProcesadosReducido/cantidadDatos}")
