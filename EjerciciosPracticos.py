#Ejercicio MAP
print("-----------------------EJERCICIOS MAP-----------------------")
# 1 -> Dada una lista de números, obtener una nueva lista con el cuadrado de cada número.
listNumeros = [1,2,3,4,5,6,7,8,9,10]
listaNumerosCuadrado = list(map(lambda x: x ** 2, listNumeros))
print(f"Lista numeros normales: {listNumeros}, lista numeros cuadrados: {listaNumerosCuadrado}")

# 2 -> Dada una lista de nombres, generar otra lista con los nombres en formato título (primera letra en mayúscula, resto en minúscula).
listaNombres = ["pedro","juan","pablo","sebastian"]
listaNombresTitulos = list(map( lambda x: x.capitalize() ,listaNombres))
print(f"Lista nombres {listaNombres}, lista nombres en mayuscula: {listaNombresTitulos}")

# 3 -> Convertir una lista de temperaturas en Celsius a Fahrenheit.
listTemperaturaCelsius = [-12,3,7,14,19,23,29,34,41,48]
listTemperaturaFahrenheit = list(map(lambda x: x * 9/5 + 32, listTemperaturaCelsius))
print(f"Lista temperatura Celsius: {listTemperaturaCelsius}, y estos serian sus iguales en Fahrenheit: {listTemperaturaFahrenheit}")

print("\n-----------------------EJERCICIOS FILTER-----------------------")
# 4 -> Filtrar de una lista de números solo los que sean números pares.
listNumeros2 = [1,2,3,4,5,6,7,8,9,10]
listNumerosPares = list(filter(lambda x: x % 2 == 0, listNumeros2))
print(f"Lista numeros 2: {listNumeros2}, lista numeros pares: {listNumerosPares}")

# 5 -> De una lista de palabras, quedarse únicamente con las que tengan más de 5 letras.
listPalabras = ["Lista", "De", "Palabras", "Para", "La", "Practica"]
listPalabrasMas5Letras = list( filter ( lambda x : len(x) > 5, listPalabras))
print(f"Lista palabras: {listPalabras}, lista palabras mas de 5 letras:{listPalabrasMas5Letras}")

# 6 -> Filtrar una lista de edades para obtener únicamente las personas que son mayores de edad (≥ 18 años).
listEdades = [12,15,61,2,5,12,55,51,4,51,1,2]
listEdadesMayores = list(filter(lambda x: x>=18, listEdades))
print(f"Lista edades: {listEdades}, lista Edades Mayores: {listEdadesMayores}")

print("\n-----------------------EJERCICIOS REDUCE-----------------------")
#importar libreria
from functools import reduce

# 7-> Calcular la suma de todos los elementos en una lista de números.
listNumeros3 = [12,15,16,26,57,3,23,63,2,52]
sumaNumeros = reduce( lambda x, y : x+y, listNumeros3)
print(f"Lista de numeros {listNumeros3}, suma Numeros: {sumaNumeros}")

# 8-> Concatenar en un solo string todas las cadenas de una lista, separadas por una coma.
listPalabras_2 = ["Lista", "De", "Palabras", "Para", "La", "Practica"]
concatenarListPalabras_2 = reduce(lambda x, y : x+","+y, listPalabras_2)
print(f"Lista palabras 2: {listPalabras_2}, lista concatenada: {concatenarListPalabras_2}")

# 9-> Encontrar el número mayor en una lista utilizando reduce.
listNumerosReduce = [12,15,16,31,41,71,91,80,5,12,41]
numeroMayor = reduce(lambda x, y: x if x>y else y, listNumerosReduce)
print(f"Lista numeros {listNumerosReduce}, numero mayor: {numeroMayor}")

print("\n-----------------------EJERCICIOS COMBINADOS-----------------------")
# 10-> A partir de una lista de números, generar una lista con sus cuadrados y luego filtrar los que sean mayores a 50.
listNumerosAlAzar = [10,7,2,5,1,8,12,62,6,11,15,17]
listNumerosAlAzarCuadrados = list(map (lambda x: x**2, listNumerosAlAzar))
listNumerosAlAzarCuadradosFiltrados = list(filter( lambda x: x>50, listNumerosAlAzarCuadrados))
print(f"Lista numeros al Azar: {listNumerosAlAzar}, lista Numeros Al Azar Cuadrados: {listNumerosAlAzarCuadrados}, Filtrados mayores a 50: {listNumerosAlAzarCuadradosFiltrados}")

# 11->Tomar una lista de frases y devolver la suma total de caracteres de todas las frases.
listaFrase = ["No cuentes los días, haz que los días cuenten.", "A veces perder es la mejor forma de empezar de nuevo.", "Lo simple también puede ser increíble.", "Hoy puede ser un gran día, todo depende de ti.", "No todo lo que brilla es oro, pero puede ser una buena idea.", "Sonríe… es gratis y mejora todo.", "Hazlo con miedo, pero hazlo.", "Las ideas no sirven de nada si no las ejecutas.", "La rutina también puede tener magia.", "No es suerte, es constancia."]
listaFraseNumeroCaracteres = list(map (lambda x: len(x), listaFrase))
listaFraseTotalCaracteres = reduce(lambda x, y: x+ y,listaFraseNumeroCaracteres)
print(f"Lista frases: {listaFrase}, lista numero caracteres por frase: {listaFraseNumeroCaracteres}, numero de caracteres total: {listaFraseTotalCaracteres}")

# 12->Generar una lista con las longitudes de cada palabra de una lista y luego obtener el máximo de esas longitudes.
palabras = ["python3", "map", "filtrado", "reducido", "lambda"]
listaLongitudPalabras = list(map( lambda x: len(x), palabras))
valorMaximoLongitud = reduce(lambda x, y: x if x > y else y, listaLongitudPalabras)
print(f"Lista de palabras: {palabras}, lista longitud de palabras: {listaLongitudPalabras}, valor maximo de longitud {valorMaximoLongitud}")

print("\n-----------------------EJERCICIOS CON GENERADORES -----------------------")
# 1 -> Crea un generador que devuelva los números pares desde 0 hasta n.
def pares_hasta(n):
    for i in range (n+1):
        if i % 2 == 0:
            yield i
for numero in pares_hasta(10):
    print(numero)

# 2 -> Crea un generador que produzca la sucesión de Fibonacci indefinidamente.
def fibonacci():
    a, b = 0, 1
    while True: 
        yield a
        a, b = b, a + b
# Tomamos solo los primeros 10 números de la sucesión
from itertools import islice
for num in islice(fibonacci(), 10):
    print(num)

# 3 -> Implementa un generador que reciba una lista de frases y devuelva solo las que tengan más de 20 caracteres.
def frases_largas(lista, minimo=20):
    for frase in lista:
        if len(frase) > minimo:
            yield frase
listaFrase = [
    "Hola mundo",
    "Python es muy poderoso",
    "Los generadores permiten trabajar con flujos de datos",
]
for f in frases_largas(listaFrase):
    print(f)

print("\n-----------------------EJERCICIOS CON ITERADORES PEREZOSOS -----------------------")
# 4-> Usa map para transformar un flujo infinito de números en sus cuadrados y toma solo los primeros 10.
from itertools import count, islice

# count() genera números infinitos (0, 1, 2, 3, ...)
numeros = count(1)
# map aplica la función a cada número (lazy, no crea lista)
cuadrados = map(lambda x: x * x, numeros)
# Tomamos solo los primeros 10
for n in islice(cuadrados, 10):
    print(n)

# 5-> Usa filter sobre un flujo de números del 1 al 100 para quedarte solo con los múltiplos de 7.
numeros = range(1, 51)
multiplo7 = filter(lambda x: x % 7 == 0, numeros)
for n in multiplo7:
    print(n)

# 6-> Combina map y filter para generar un flujo con los cuadrados de los números impares del 1 al 20.
# Primero filtramos los impares, luego calculamos el cuadrado
numeros = range(1, 21)
impares = filter(lambda x: x % 2 != 0, numeros)
cuadrados_impares = map(lambda x: x * x, impares)
print(list(cuadrados_impares))


print("\n-----------------------EJERCICIOS CON ITERTOOLS -----------------------")
# 7-> Genera un flujo infinito de números con itertools.count() y corta cuando llegues a 50.
from itertools import count, takewhile
# count(1) genera 1, 2, 3, 4, ...
numeros = count(1)
# takewhile corta cuando se cumple la condición
hasta_50 = takewhile(lambda x: x <= 50, numeros)
print(list(hasta_50))

# 8-> Usa itertools.cycle() para repetir indefinidamente una lista de colores (["rojo", "verde", "azul"]) y toma los primeros 7 valores.
from itertools import cycle, islice
colores = ["rojo", "verde", "azul"]
# cycle() repite infinitamente
ciclo_colores = cycle(colores)
# islice() corta los primeros 7 elementos
primeros_7 = list(islice(ciclo_colores, 7))
print(primeros_7)

# 9-> Usa itertools.islice() para extraer un fragmento de un flujo de Fibonacci (por ejemplo, del 5° al 15° término).
from itertools import islice
# Generador de Fibonacci
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# Extraemos del 5º al 15º término
fragmento = list(islice(fibonacci(), 5, 16))  # índice inicio=5, fin=16
print(fragmento)