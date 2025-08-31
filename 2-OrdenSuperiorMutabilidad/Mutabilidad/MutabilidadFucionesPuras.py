"""
Mutabilidad significa que un objeto puede cambiar su contenido después de haber sido creado.
Inmutabilidad significa que un objeto NO puede cambiar su contenido: si quieres otro valor, 
tienes que crear un nuevo objeto.
"""

#Mutables: listas, diccionarios, conjuntos
# Lista (mutable)
numeros = [1, 2, 3]
print("Antes:", numeros)

# Modificamos la lista
numeros[0] = 99
numeros.append(4)
print("Después:", numeros)
#La misma lista cambió su contenido

#Inmutables: enteros, flotantes, cadenas, tuplas
# String (inmutable)
nombre = "Juan"
print("Antes:", nombre)

# Intentamos modificarlo (esto da error)
# nombre[0] = "P"   ❌
# La única forma es crear un NUEVO string
nombre = "Pedro"
print("Después:", nombre)
#No se puede cambiar el contenido directamente, solo reemplazar por un nuevo objeto

"""
Funciones Puras:
1. Siempre devuelve el mismo resultado si le das las mismas entradas.
2. No modifica nada fuera de ella (no cambia variables globales, ni escribe en disco, ni imprime).
"""
#Ejemplo de funcion pura
def cuadrado(x):
    return x * x

print(cuadrado(4))  # 16
print(cuadrado(4))  # 16 (siempre igual)

#Funcion impura
contador = 0
def incrementar():
    global contador
    contador += 1
    return contador
print(incrementar())  # 1
print(incrementar())  # 2 (cambia cada vez)