"""
La evaluación perezosa es una técnica en la que una expresión no se evalúa inmediatamente cuando se define, sino hasta que su valor es realmente necesario.
Esto evita cálculos innecesarios y permite trabajar con estructuras de datos infinitas o muy grandes sin que el programa se bloquee o consuma toda la memoria.

Caracteristicas
 - Solo se calcula cuando se necesita
 - Ahorra recursos si no se usan todos los valores
 - Permite trabajar con colecciones infinitas (generadores, iteradores)

"No hace un calculo hasta que realmente sea necesario"

"""

# Ejemplo N1: Generador que produce números del 1 al infinito (no se evalúa todo de una vez)
def numeros():
    n = 1
    while True:
        print(f"Generando {n}")
        yield n
        n += 1

# Solo se calculan cuando se piden
gen = numeros()

print(next(gen))  # Evalúa solo el primer número
print(next(gen))  # Evalúa solo el segundo
print(next(gen))  # Evalúa solo el tercero


# Ejemplo N2: Imagina que tienes una lista de 10.000 números, y quieres saber si alguno es mayor a 50.
# Sin pereza: El computador revisa todos los 10.000 números y después dice: "sí, hay uno mayor a 50".

# Crear una lista de números (del 1 al 1 millón)
numeros = [n for n in range(1, 1000001)]
# Preguntar si existe un número mayor a 50
print(any(n > 50 for n in numeros))

# Con pereza: El computador revisa uno por uno, pero se detiene en el momento en que encuentra uno mayor a 50. No revisa los demás.
# Crear un generador (no guarda todos los números, los genera cuando se necesitan)
numeros = (n for n in range(1, 1000001))
# Preguntar si existe un número mayor a 50
print(any(n > 50 for n in numeros))

#Ejemplo N3: Imagina que tienes cajas con manzanas numeradas del 1 al infinito 🍎
def manzanas():
    n = 1
    while True:      # bucle infinito
        yield n      # genera el número cuando lo piden
        n += 1

# Generamos manzanas infinitas (nunca se acaban)
caja = manzanas()

# Buscamos la primera manzana mayor que 100
for m in caja:
    if m > 100:
        print("Encontré la manzana:", m)
        break

# Ejemplo N4: La lista completa (sin pereza)
# Creamos una lista de números del 1 al 10
numeros = [n for n in range(1, 11)]
print(numeros)  # Muestra toda la lista Esto NO es perezoso, porque ya calculó todo antes de que yo lo pidiera.

#Generador (con pereza)
# Creamos un generador de números del 1 al 10
numeros = (n for n in range(1, 11))
print(numeros)  # No muestra los números directamente

# Ejemplo N5: Usando el generador paso a paso
# Generador perezoso de números del 1 al 10
numeros = (n for n in range(1, 11))
# Obtener el primer número
print(next(numeros))  
# Obtener el segundo número
print(next(numeros))  
# Obtener el tercero
print(next(numeros))

# Ejemplo N6: Búsqueda rápida (ventaja de la pereza)
#Imagina que quiero saber si existe un número mayor que 5.
numeros = (n for n in range(1, 11))  # Generador del 1 al 10

for n in numeros:
    print("Probando:", n)
    if n > 5:
        print("¡Encontrado!", n)
        break

# Numero N7: Generador infinito
def contar():
    n = 1
    while True:   # Nunca termina
        yield n   # Devuelve el valor actual
        n += 1    # Pasa al siguiente número

# Creamos un generador infinito
numeros = contar()

print(next(numeros))  # 1
print(next(numeros))  # 2
print(next(numeros))  # 3
