#Importar libreria reduce
from functools import reduce

# 1 -> Genere de forma perezosa los números pares desde 2 hasta 200 millones.
def generadorNumeros():
    n = 2
    while True:
        yield n
        n += 2
    
# 2 -> Consuma los primeros 500 números generados y guárdelos en una lista.
# (Pista: usa next en un bucle)
consumidor = generadorNumeros()
print()
listaSegunda = []
for i in range(500):
    nuevoNumero = next(consumidor)    
    listaSegunda.append(nuevoNumero)
print(f"2 -> {listaSegunda}")

# 3 -> Filtre solo aquellos que sean múltiplos de 7 y cuya suma de dígitos sea mayor que 15.
# (Pista: str(x) y sum(int(d) for d in str(x)))
print()
listaTres = list(filter(lambda x: x % 7 == 0 and sum(int(d) for d in str(x)) > 15, listaSegunda))
print(f"3 -> {listaTres}")

# 4 -> Transforme cada número filtrado elevándolo a la cuarta potencia.
print()
listaCuatro = list(map(lambda x: x ** 4, listaTres))
print(f"4 -> {listaCuatro}")

# 5 -> Consuma únicamente los primeros 40 resultados transformados.
print()
listaCinco = list(map(lambda x: x, listaCuatro[:40]))
print(f"5 -> {listaCinco}")

# 6 -> Calcule la suma total y el valor máximo de esos resultados.
print()
listaSeis = reduce(lambda x, y: x+y, listaCinco)
valor_maximo = max(listaCinco)
print(f"6 -> Suma Total: {listaSeis}, Valor Máximo: {valor_maximo}")