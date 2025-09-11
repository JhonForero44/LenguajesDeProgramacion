# Importar librería
from functools import reduce

# 1 -> Generador de números hasta un límite dado
#def generador_numeros(limite):
#    for i in range(1, limite + 1):
#        yield i
#numeros = generador_numeros(20)

# 1 -> Genere de forma perezosa los números desde 1 hasta 1000.
# (Pista: use yield)
def generadorNumeros():
    n = 1
    while True:
        yield n
        n += 1

consumidor = generadorNumeros()
        
# 2 -> Consuma los primeros 200 números generados y guárdelos en una lista.
print()
listaDos = []
for i in range(200):
    nuevoNumero = next(consumidor)
    listaDos.append(nuevoNumero)
print(f"Lista 2 -> {listaDos}")

# 3 -> Filtre solo aquellos que sean múltiplos de 5 y cuya suma de dígitos sea menor que 10.
print()
listaTres = list(filter(lambda x: x % 5 == 0 and sum(int(d) for d in str(x)) < 10, listaDos))
print(f"Lista 3 -> {listaTres}")

# 4 -> Transforme cada número filtrado elevándolo al cuadrado.
print()
listaCuatro = list(map(lambda x: x ** 2, listaTres))
print(f"Lista 4 -> {listaCuatro}")

# 5 -> Consuma únicamente los primeros 25 resultados transformados.
print()
listaCinco = list(map(lambda x: x, listaCuatro[:25]))
print(f"Lista 5 -> {listaCinco}")

# 6 -> Calcule la suma total y el valor mínimo de esos resultados.
print()
listaSeis = reduce(lambda x, y: x + y, listaCinco)
numeroMenor = min(listaCinco)
print(f"Lista 6 -> {listaSeis} y el numero menor es: {numeroMenor}")

# 7 -> Genere un correo electrónico para cada número:
#       - Si el número es par -> Outlook
#       - Si el número es impar -> Gmail
# (Formato: user{numero}@dominio.com)
print()

listaGmail = []
listaOutlook = []

for i in listaDos:
    if i % 2 == 0:
        listaOutlook.append(f"usuario{i}@outlook.com")
    else:
        listaGmail.append(f"usuario{i}@gmail.com")        

#lista_correos = list(map(lambda x: f"user{x}@outlook.com" if x % 2 == 0 else f"user{x}@gmail.com", lista_numeros))

print(f"Lista Outlook -> {listaOutlook}")
print()
print(f"Lista Gmail -> {listaGmail}")