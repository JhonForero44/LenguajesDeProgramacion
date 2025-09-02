"""
Un flujo de datos es una secuencia de datos que se procesa de forma continua y bajo demanda.
En lugar de cargar toda la información en memoria, se procesa en fragmentos o registros a medida que llegan (similar a cómo funcionan los archivos grandes o los datos en tiempo real).
Características:
- Manejo de grandes volúmenes de datos sin cargarlos completos.
- Útil para procesar datos en tiempo real (ej. sensores, logs, streaming de video).
- Se pueden combinar con la evaluación perezosa.

Imagina que tienes tuberías de agua 🚰.
- El agua son los datos (información).
- Las tuberías son los caminos que sigue esa información.
- En cada tramo de la tubería, puedes transformar el agua: filtrarla, calentarla, enfriarla, etc.
En informática, eso se llama flujo de datos → el recorrido que hace la información desde que aparece hasta que llega a su destino, pasando por pasos intermedios.
"""

# Ejemplo N1: Supongamos que tenemos un archivo de texto muy grande
# Lo leemos como flujo de datos (una línea a la vez)
"""
def leer_archivo_en_flujo(ruta):
    with open(ruta, "r") as archivo:
        for linea in archivo:
            yield linea.strip()  # Lazy: solo genera una línea cuando se pide

# Ejemplo de uso
for i, linea in enumerate(leer_archivo_en_flujo("archivo_grande.txt")):
    print(linea)
    if i == 4:  # Solo leemos las primeras 5 líneas, el resto nunca se carga
        break

"""

# Ejemplo N2: Supongamos que tienes una lista de frutas ["manzana", "pera", "banano", "uva"]
# 1->El flujo de datos podría ser:
# 2->Recibo todas las frutas.
# 3->Me quedo solo con las que tengan más de 5 letras.
# 4->Las convierto en MAYÚSCULAS.
# 5->Muestro el resultado.

# Paso 1: tengo mis datos (como la canasta de frutas)
frutas = ["manzana", "pera", "banano", "uva"]           # frutas → es como la canasta original.
# Paso 2: filtro las frutas que tengan más de 5 letras
frutas_filtradas = [f for f in frutas if len(f) > 5]    # frutas_filtradas → solo dejo las que cumplen una condición (más de 5 letras).
# Paso 3: convierto esas frutas a mayúsculas
frutas_mayus = [f.upper() for f in frutas_filtradas]    # frutas_mayus → transformo lo que queda (poner en mayúsculas).
# Paso 4: muestro el resultado
print(frutas_mayus)                                     # print → saco el resultado final.

# Ejemplo N2: Imagina que tienes números en una lista y quieres
# 1-> Tomar solo los pares.
# 2-> Multiplicarlos por 2.
# 3-> Mostrar el resultado.

numeros = [1, 2, 3, 4, 5, 6]
# Tomo solo los pares
pares = [n for n in numeros if n % 2 == 0]
# Multiplico cada par por 2
resultado = [n * 2 for n in pares]
print(resultado) # [4, 8, 12]

# Ejemplo N3: Nombres y longitud
# Imagina que tienes una lista de nombres y quieres saber cuáles son largos (más de 4 letras).

# Lista inicial: los datos de entrada
nombres = ["Ana", "Luis", "Mariana", "Sofía"]
# Paso 1: me quedo con los nombres largos (más de 4 letras)
nombres_largos = [n for n in nombres if len(n) > 4]
# Paso 2: muestro los resultados
print(nombres_largos)   # ['Mariana', 'Sofía']

# Ejemplo N4: Calificaciones de estudiantes
# Ahora supongamos que tienes calificaciones y quieres quedarte solo con las que son mayores o iguales a 3 (aprobados).

# Datos iniciales: calificaciones
notas = [2.5, 3.0, 4.5, 1.8, 5.0]
# Paso 1: filtro los aprobados
aprobados = [n for n in notas if n >= 3]
# Paso 2: muestro el resultado
print(aprobados) # [3.0, 4.5, 5.0]

# Ejemplo N5: Calificaciones de estudiantes
# Tienes precios de productos y quieres aplicar un 10% de descuento a cada uno.

# Datos iniciales: precios
precios = [100, 250, 80, 50]
# Paso 1: aplico un descuento del 10%
precios_descuento = [p * 0.9 for p in precios]
# Paso 2: muestro el resultado
print(precios_descuento)    # [90.0, 225.0, 72.0, 45.0]

# Ejemplo N6: Contar letras en palabras
# Ahora quieres contar cuántas letras tiene cada palabra en una lista.

# Datos iniciales: palabras
palabras = ["sol", "luna", "estrella"]
# Paso 1: creo una lista con el número de letras de cada palabra
longitudes = [len(p) for p in palabras]
# Paso 2: muestro el resultado
print(longitudes)   # [3, 4, 8]

