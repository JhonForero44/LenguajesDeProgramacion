#EJERCICIO 2: (lazy evaluation, map, filter, reduce)
# GENERE DE FORMA PEREZOSA LOS NUMEROS HASTA 50000000
def generadorNumeros():
    for i in range(50000000):
        yield i            

#Creando generador
gen_numeros = generadorNumeros()

#Pedimos los primeros 100:
nums = []
for i in range(100):
    nuevo_num = next(gen_numeros)
    nums.append(nuevo_num)

print()
print("-------- EJERCICIO N2 --------")    
# FILTRE SOLO AQUELLOS QUE SEAN MULTIPLOS DE 5
listaFiltradaNUmeros_5 = list(filter ( lambda x: x % 5 ==0, nums))
print(listaFiltradaNUmeros_5)

# TRANSFORME CADA NUMERO FILTRADOS ELEVANDOLO AL CUADRADO
listaFiltradaNUmeros_5_Cuadrado = list(map(lambda x: x**2, listaFiltradaNUmeros_5))
print(listaFiltradaNUmeros_5_Cuadrado)

# CONSUM SOLO LOS PRIMEROS 10 RESULTADOS 
listaConsumo = list(map( lambda x : x, listaFiltradaNUmeros_5_Cuadrado[:10]))
print(listaConsumo)

# CALCULE LA SUMA DE ESOS 10 RESULTADOS PROCESADOS
from functools import reduce
sumaTotalConsumido = reduce(lambda x, y: x + y, listaConsumo)
print(f"Suma total: {sumaTotalConsumido}")