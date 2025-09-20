#Procedimiento:
#Su programa debe cargar los datos desde el csv iterando sobre cada renglón y usando la función dict y zip. No se permite el uso de CSVReader o DictReader.
#Cada registro del dataset debe ser un diccionario con los campos especificados en el encabezado del archivo plano.
#El lector de datos debe devolver solo un registro a la vez y esperar a que lo consuman (lazy generator)
def lectorDatos(archivo):
    with open(archivo) as file:
        headers = file.readline().strip().split(",")
        for line in file:
            values = line.strip().split(",")
            record = dict(zip(headers, values))
            yield record

#Cargar dataset
cargarDataset = lectorDatos("datos.csv")
#Consumidor, cargar datos del dataset
datosDataset = []

try:
    pass
    for _ in range(7):
        nuevoDato = next(cargarDataset)
        datosDataset.append(nuevoDato)
except StopIteration:
    print("Valor ingresados incorrectamente.")

print(f"Dataset Original: {datosDataset}")

#Analisis del Dataset
#El análisis del dataset incluye:
#filtrar personajes con nivel > 10 usando una función lambda
filtroPersonajesaNiveles = list(filter(lambda x: int(x["nivel"]) > 10 , datosDataset))
print()
print(f"1 Filtro nivel mayor a 10 -> {filtroPersonajesaNiveles}")

#usar map con una función lambda para crear una nueva lista donde se tenga un campo adicional "totalPower", que se calcule como ataque + defensa
listaTotalPower = list(map(lambda x: {"totalPower": int(x["ataque"]) + int(x["defensa"]), **x}, filtroPersonajesaNiveles))
print()
print(f"2 Lista nuevo Campo -> {listaTotalPower}")

#obtener el personaje con mayor poder total de todo el dataset usando reduce
from functools import reduce
print()
personajeMayorPoder = reduce( lambda x, y: x if x["totalPower"] > y["totalPower"] else y, listaTotalPower)
print(f"3 Personaje Mayor Poder -> {personajeMayorPoder}")