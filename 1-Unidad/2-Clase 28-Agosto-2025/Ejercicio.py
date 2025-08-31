from functools import reduce
#EJERCICIO
lista = ["muchos", "años", "después", "frente", "al", "pelotón", "de", "fusilamiento", "el", "coronel", "aureliano", "buendía", "había", "de", "recordar", "aquella", "tarde", "remota", "en", "que", "su", "padre", "lo", "llevó", "a", "conocer", "el", "hielo"]

# 1. Convertir a mayusculas, todas las palabas  de la lista
listaMayuscula = list(map(lambda x: x.upper(), lista))
print(f"Lista en Mayuscula: {listaMayuscula}")

# 2. Armar un solo texto 
lista_reducida = reduce(lambda x, y: x + " " + y, lista)
print(f"Armar un solo texto: {lista_reducida}")