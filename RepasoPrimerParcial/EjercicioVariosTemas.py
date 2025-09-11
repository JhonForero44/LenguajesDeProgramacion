# Ejercicio Practica
print()
print("----------------- EJERCICIO NUMERO 1 -----------------")
# 1-> Genere de forma perezosa los números impares hasta 30 millones.
def generarNumeros():
    for i in range(30000000):
        yield i + 1

#Creando Generador
generadorNumero = generarNumeros()

#Obtener los primeros 200 numeros    
listaNumeros = []
for i in range(200):
    nuevo_Numero = next(generadorNumero)
    listaNumeros.append(nuevo_Numero)
print(listaNumeros)

# 2-> Filtre solo aquellos que sean múltiplos de 7.
listaFiltradaMultiplosSiete = list(filter(lambda x: x % 7 == 0, listaNumeros))
print()
print(listaFiltradaMultiplosSiete)

# 3-> Transforme cada número filtrado sumándole 3.
listaFiltradaMultiplosSieteSumandoleTres = list(map(lambda x: x + 3, listaFiltradaMultiplosSiete))
print()
print(listaFiltradaMultiplosSieteSumandoleTres)

# 4-> Consuma solo los primeros 15 resultados procesados.
listaFiltradaMultiplosSieteSumandoleTresQuincePrimeros = list(map(lambda x: x, listaFiltradaMultiplosSieteSumandoleTres[:15]))
print()
print(listaFiltradaMultiplosSieteSumandoleTresQuincePrimeros)

# 5-> Calcule el producto de esos 15 resultados.
from functools import reduce
listaFiltradaMultiplosSieteSumandoleTresQuincePrimerosReducido = reduce(lambda x, y : x * y, listaFiltradaMultiplosSieteSumandoleTresQuincePrimeros)
print()
print(listaFiltradaMultiplosSieteSumandoleTresQuincePrimerosReducido)

# Ejercicio Practica
print()
print("----------------- EJERCICIO NUMERO 2 -----------------")
# 1-> Genere de forma perezosa los números hasta 40 millones.
def generadorPerezoso():
    for i in range(40000000):
        yield i + 1

#Consumidos
consumidorGenerador = generadorPerezoso()

#Generar los primeros 500 Numeros
listaNumerosQuinientos = []

for i in range(500):
    agregarNumeros = next(consumidorGenerador)
    listaNumerosQuinientos.append(agregarNumeros)
print(f"Primera Lista: {listaNumerosQuinientos}")    

# 2-> Filtre solo aquellos que sean números pares y múltiplos de 9.
segundaLista = list(filter(lambda x: x % 2 == 0 | x % 9 == 0, listaNumerosQuinientos))
print(f"Segunda Lista: {segundaLista}")

# 3-> Transforme cada número filtrado calculando su raíz cuadrada.
terceraLista = list(map(lambda x: x ** 1/2, segundaLista))
print(f"Tercera Lista: {terceraLista}")

# 4-> Consuma solo los primeros 20 resultados procesados.
cuartaLista = list(map(lambda x: x, terceraLista[:20]))
print(f"Cuarta Lista: {cuartaLista}")

from functools import reduce
# 5-> Calcule la suma de esos 20 resultados.
quintaLista = reduce(lambda x,y: x + y, cuartaLista)
print(f"Quinta Lista: {quintaLista}")