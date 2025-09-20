# -----------------------------------------------------------------------------
# Lector lazy (generador) de registros desde un CSV plano (sin usar csv.DictReader)
# -----------------------------------------------------------------------------
def lectorDatos(archivo):
    # Abre el archivo en modo lectura. (Recomendable añadir encoding="utf-8")
    with open(archivo) as file:
        # Lee la primera línea: se espera que sea el encabezado (headers),
        # por ejemplo: "nombre,nivel,clase,ataque,defensa"
        # strip() quita '\n' y espacios; split(",") separa por comas -> lista de encabezados
        headers = file.readline().strip().split(",")

        # Itera el resto de líneas del archivo una por una (esto es lazy: no carga todo en memoria)
        for line in file:
            # strip() elimina saltos de línea y espacios al inicio/fin;
            # split(",") separa cada campo en la línea
            values = line.strip().split(",")

            # zip(headers, values) empareja cada encabezado con su correspondiente valor
            # dict(...) convierte ese par de pares en un diccionario: {header1: value1, ...}
            # IMPORTANTE: si la línea tiene más/menos campos que headers, zip truncará al menor.
            record = dict(zip(headers, values))

            # yield devuelve un registro (diccionario) y "pausa" la función hasta el próximo next()
            yield record


# -------------------------
# Consumidor: cargar dataset
# -------------------------
# Llamar a la función generadora NO lee el archivo aún; devuelve un iterador generador.
cargarDataset = lectorDatos("datos.csv")

# Lista donde acumularemos los registros consumidos del generador
datosDataset = []

try:
    pass  # aquí no hace nada; la línea 'pass' es innecesaria pero no altera el flujo

    # Se intenta consumir exactamente 7 registros del generador:
    # - for _ in range(7): repetirá 7 veces
    # - next(cargarDataset) pide "el siguiente" registro al generador
    # Si el generador se agota antes de 7 registros, next(...) lanzará StopIteration
    for _ in range(7):
        nuevoDato = next(cargarDataset)
        datosDataset.append(nuevoDato)

# Se captura la excepción que ocurre si el generador no tiene suficientes registros
except StopIteration:
    # Mensaje informando que no se pudieron obtener los 7 valores solicitados
    print("Valor ingresados incorrectamente.")

# Muestra por pantalla los registros acumulados hasta ahora
print(f"Dataset Original: {datosDataset}")


# -------------------------
# Análisis del Dataset
# -------------------------
# Filtrar personajes con nivel > 10 usando filter + lambda
# - filter devuelve un iterador con elementos que cumplan la condición
# - aquí convertimos x["nivel"] a int porque el campo viene como string del CSV
filtroPersonajesaNiveles = list(filter(lambda x: int(x["nivel"]) > 10 , datosDataset))
print()
print(f"1 Filtro nivel mayor a 10 -> {filtroPersonajesaNiveles}")


# Usar map con lambda para crear una nueva lista donde cada registro tenga
# una clave adicional "totalPower" = ataque + defensa.
# - map aplica la lambda a cada elemento del iterable; devolvemos un nuevo diccionario
# - NOTA SOBRE EL ORDEN: {"totalPower": ..., **x} --> **x viene DESPUÉS y puede sobrescribir
#   el campo "totalPower" si x ya lo tenía. Si quieres asegurarte que el valor calculado
#   prevalezca, usa {**x, "totalPower": ...}
listaTotalPower = list(map(lambda x: {"totalPower": int(x["ataque"]) + int(x["defensa"]), **x}, filtroPersonajesaNiveles))
print()
print(f"2 Lista nuevo Campo -> {listaTotalPower}")


# Obtener el personaje con mayor poder total usando reduce
from functools import reduce
print()
# - reduce toma dos elementos a la vez (x, y) y devuelve el 'mejor' según la condición
# - al final reduce devuelve un único registro: el que tiene mayor "totalPower"
personajeMayorPoder = reduce( lambda x, y: x if x["totalPower"] > y["totalPower"] else y, listaTotalPower)
print(f"3 Personaje Mayor Poder -> {personajeMayorPoder}")
