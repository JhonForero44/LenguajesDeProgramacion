#Funciones como primer orden
print("----------- FUNCIONES DE PRIMER ORDEN -----------")

# 1-> Define una función que calcule el cuadrado de un número y asígnala a una variable. Usa esa variable para calcular el cuadrado de varios números.
def cuadrado(x):
    return x ** 2

cuadrado_n1 = cuadrado(2)
cuadrado_n2 = cuadrado(3)
cuadrado_n3 = cuadrado(4)
cuadrado_n4 = cuadrado(5)
print(f"El primer cuadrado es: {cuadrado_n1}, el segundo cuadrado es: {cuadrado_n2}, el tercer cuadrado es: {cuadrado_n3}, el cuarto cuadrado es: {cuadrado_n4}")

# 2 -> Crea una función que reciba otra función y un número, y aplique esa función dos veces sobre el número.
def funcion_dos(funcion, numero):
    return funcion(funcion(numero))

def suma(num):
    return num + num

print(funcion_dos(suma, 8))

# 3-> Implementa una función que devuelva otra función que sume un valor fijo a cualquier número.
def devolverFuncion(valor_fijo):
    def suma_fija(numero):
        return numero + valor_fijo
    return suma_fija

suma_dos = devolverFuncion(5)
print(f"Funcion 3 -> {suma_dos(2)}")

#Lambda
print()
print("----------- FUNCIONES LAMBDA -----------")
# 4-> Escribe una expresión lambda que reciba dos números y devuelva el mayor.
numeroMayor = lambda x,y : x if x > y else y
print(f"El numero mayor entre 3 y 4 es: {numeroMayor(3,4)}")
print(f"El numero mayor entre 1 y 8 es: {numeroMayor(1,8)}")
print(f"El numero mayor entre 96 y 10 es: {numeroMayor(96,10)}")

# 5-> Usa map() con una función lambda para convertir una lista de temperaturas en Celsius a Fahrenheit.
datosCelsius = [-20, -10, 0, 10, 20, 25, 30, 37, 40, 100]
datosFahrenheit = list(map(lambda x : (x*9/5)+32 , datosCelsius))
print(f"Lista de datos en Celsius: {datosCelsius}, Lista de datos en Fahrenheit: {datosFahrenheit}")

# 6-> Usa filter() con una lambda para obtener todas las palabras que empiecen con vocal de una lista de strings.
palabrasString_2 = ["Hola", "Expulsion", "Barcelona", "Messi", "Colombia", "Repaso", "Parcial"]
palabrasString_2_vocales = list(filter(lambda x: x[0].lower() in "aeiou", palabrasString_2))
print(f"Lista String 2: {palabrasString_2}, lista vocales string 2: {palabrasString_2_vocales}")

#Funciones Puras
print()
print("----------- FUNCIONES PURAS -----------")
# 7 -> Implementa una función pura que convierta una lista de enteros en una lista con cada entero elevado al cubo.
listaEnteros = [1,2,3,4,5,6,7,8,9,10]
def convercionLista(lista):
    return [x ** 3 for x in lista]

print(convercionLista(listaEnteros))
    
# 8 -> Crea una función impura que modifique una lista global y otra función pura que devuelva una nueva lista sin modificar la original.
# Lista global
listaGlobal = [1, 2, 3, 4, 5]

# Función impura que modifica la lista global
def modificarListaGlobal():
    listaGlobal.append(44)

# Función pura que devuelve una nueva lista sin modificar la original
def nuevaLista(lista):
    # Creamos una nueva lista con el valor añadido
    return lista + [99]

# Usamos la función impura para modificar la lista global
modificarListaGlobal()

# Usamos la función pura para crear una nueva lista sin modificar la original
nueva_lista = nuevaLista(listaGlobal)

print("Lista Global modificada:", listaGlobal)  # Lista original con 44 añadida
print("Nueva Lista:", nueva_lista)  # Lista nueva con 99 añadida sin modificar la original

# 9 -> Diseña una función pura que, dado un número, indique si es primo o no.
def es_primo(n):
    if n <= 1:
        return False  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False  
    return True  

numero = 29
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

#Funciones de Orden Superior
print()
print("----------- ORDEN SUPERIOR -----------")

# 10 ->  Crea una función que reciba otra función y una lista, y devuelva una nueva lista con la función aplicada a cada elemento.
listaNumeroDiez = [1,2,3,4,5,6,7,8,9,11,22,33]
def sumarLosNumeros(num):
    return num + 3    

def primera_funcion(funcion, lista):
    return [funcion(num) for num in lista] 

resultado = primera_funcion(sumarLosNumeros, listaNumeroDiez)
print(f"Lista numero Diez: {listaNumeroDiez}, numeros sumados: {resultado}")

# 11 -> Escribe una función que reciba una lista de funciones y un valor, y devuelva el resultado de aplicar todas las funciones en orden al valor.
# Función que aplica una lista de funciones al valor en orden
def aplicar_funciones(funciones, valor):
    for funcion in funciones:
        valor = funcion(valor)  # Aplica la función al valor y actualiza el valor
    return valor

# Ejemplo de funciones
def suma_3(num):
    return num + 3

def multiplica_2(num):
    return num * 2

def resta_1(num):
    return num - 1

# Lista de funciones
lista_funciones = [suma_3, multiplica_2, resta_1]

# Valor inicial
valor_inicial = 5

# Aplicamos las funciones al valor inicial
resultado = aplicar_funciones(lista_funciones, valor_inicial)

# Imprimimos el resultado
print(f"Valor inicial: {valor_inicial}")
print(f"Resultado después de aplicar las funciones: {resultado}")

# 12 -> Diseña una función que devuelva otra función que multiplique sus argumentos por un número dado.
# Función que devuelve otra función que multiplica sus argumentos por un número dado
def multiplicador(n):
    def multiplicar(*args):
        return [x * n for x in args]  # Multiplica cada argumento por 'n' y devuelve una lista con los resultados
    return multiplicar

# Ejemplo de uso
multiplicar_por_3 = multiplicador(3)  # Creamos una nueva función que multiplica por 3
resultado = multiplicar_por_3(1, 2, 3, 4, 5)  # Aplicamos la función a varios números

# Imprimimos el resultado
print(f"Resultado de multiplicar por 3: {resultado}")

#map()
print()
print("----------- FUNCIONES MAP -----------")
# 13 -> Usa map() para convertir una lista de nombres en mayúsculas.
listaNombre = ["jhon","arley","forero","velasco"]
listaNombresMayuscula = list(map (lambda x: x.upper(), listaNombre))
print(f"Lista nombres normal: {listaNombre}, lista nombres Mayuscula {listaNombresMayuscula}")

# 14 -> Aplica map() para calcular la longitud de cada palabra en una lista de strings.
palabrasString = ["Una","vez","fuimos","al","parque","cada","dia","el","mas","grande","autopista"]
longitudPalabrasString = list(map(lambda x: len(x), palabrasString))
print(f"Lista de palabras: {palabrasString}, lista de longitud de palabras: {longitudPalabrasString}")

# 15 -> Crea una lista de números y usa map() con lambda para obtener sus inversos (1/n).
listaNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
listaNumerosInversos = list(map(lambda x: 1/x, listaNumeros))
print(f"Lista numeros: {listaNumeros}, lista numeros investos: {listaNumerosInversos}")

#filter()
print()
print("----------- FUNCIONES FILTER -----------")
# 16 -> Usa filter() para obtener de una lista de enteros solo los múltiplos de 3.
listaNumeros_filter = [10,16,25,235,12,612,16,12,19,6,125,56,6,23,23]
listaNumeros_filter_multiplos_tres = list(filter(lambda x: x % 3 == 0, listaNumeros_filter))
print(f"Lista numeros {listaNumeros_filter}, lista multiplos de tres: {listaNumeros_filter_multiplos_tres}")

# 17 -> Dada una lista de strings, filtra los que tengan más de 5 caracteres.
listaStrings = ["Hola","Mundo","Soy","Mordelon"]
listaStringsCincoCaracteres = list(filter(lambda x : len(x) > 5, listaStrings))
print(f"Lista Strings {listaStrings}, lista String 5 Caracteres {listaStringsCincoCaracteres}")

# 18 -> Dada una lista de diccionarios con personas (nombre, edad), usa filter() para obtener solo los mayores de 18 años.
diccionarioPersonas = {
    "Juan": 22,
    "Pedro": 21,
    "Perez": 17,
    "Oscar": 43    
}
diccionarioPersonasFiltrado = dict(filter(lambda x: x[1]>18, diccionarioPersonas.items()))
print(f"Diccionario: {diccionarioPersonas}, diccionario filtrado: {diccionarioPersonasFiltrado}")

#reduce()
print()
print("----------- FUNCIONES REDUCE -----------")
from functools import reduce
# 19 -> Usa reduce() para calcular la suma de una lista de números.
listaDeNumeros = [19,20,14,8,91,120,1204]
sumaTotallistaDeNumeros = reduce(lambda x,y : x+y, listaDeNumeros)
print(f"La lista de numeros {listaDeNumeros}, la suma total es {sumaTotallistaDeNumeros}")

# 20 -> Usa reduce() para concatenar todos los strings de una lista en una sola cadena.
palabrasString_2 = ["Una","vez","fuimos","al","parque","cada","dia","el","mas","grande","autopista"]
strings = reduce(lambda x, y: x + " " + y, palabrasString_2)
print(f"Lista string normal {palabrasString_2}, la linea completra es: {strings}")

# 21 -> Dada una lista de diccionarios con productos (nombre, precio), usa reduce() para calcular el precio total.
productos = {
    "perro" : 2000,
    "sandwich" : 3000,
    "gaseosa": 500,
    "salchipap": 6000
}

precioTotalProductosNuevos = reduce(lambda x,y: x+y, productos.values())

print(f"Lista de productos y precios: {productos}, suma total de productos: {precioTotalProductosNuevos}")