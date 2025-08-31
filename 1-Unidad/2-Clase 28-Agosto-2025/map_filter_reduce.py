from functools import reduce

#MAP: Mapea una funcion a todos los elementos de una lista, benedicio se ve con grandes datos
# EStructura -> ( Funcion, Lista)
#Ejemplo conversion de divisas (1 USD = $4100 COP)
precios_dolares = [45, 35, 25, 18, 24, 26, 47, 19]
#map solo -> objeto iterable
#Tocar converir a lista el map
precios_pesos = list(map(lambda x: x * 4100.0, precios_dolares))

print(f"Precios en dolares: {precios_dolares}")
print(f"Precios en pesos: {precios_pesos}")

#Diferencia entre map y filter:
# map: aplicacion una funcion a todos los elementos de una coleccion de datos
#      (con la condiccion que la funcion retorne un valor)
# filter: aplica una condicion a todos los elementos de una coleccion de datos.
#       Devuelve solo los elementos que cumplen con la condicion en una nueva coleccion de datos
#         (la condicion debe retornar True o False)

# B) FILTER: 
#Filtrar la lista de precios para obtener solo los precios mayores a 100000
#Estructura -> (Funcion, Lista)
lista_filtrada = list(filter(lambda x: x <= 100000.0, precios_pesos))
print(f"Lista filtrada de los precios en pesos: {lista_filtrada}")

# C) REDUCE: Reduce usando una funcion de reducion
# Generar un solo valor consolidado a partir de una coleccion de datos
# Estructura -> (Funcion, Lista)
suma_precios = reduce(lambda x, y: x + y, lista_filtrada)
print(f"Suma de los precios filtrados: {suma_precios}")