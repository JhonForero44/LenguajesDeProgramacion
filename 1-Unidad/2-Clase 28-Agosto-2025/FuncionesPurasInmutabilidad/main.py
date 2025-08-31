#Funciones PURAS E INMUTABILIDAD:
Lista_nombre = ["Diego", "Diana", "Maria", "Pedro", "Juan"]

#Sacara una copia de la lista y le agregara un nombre nuevo CONSERVANDO LA INMUTABILIDAD
lista_nombre_nueva = Lista_nombre + ["Mariana"]

#VULNERA LA INMUTABILIDAD
Lista_nombre = Lista_nombre + ["Mariana"]

print(Lista_nombre)
print(lista_nombre_nueva)

#FUNCIONES PURAS
def cubo(numero):
    return numero * numero * numero

print(f"El cubo de 4 es: {cubo(4)}")

#Funcion pura que agrega un elemento a una lista sin modificar la original
def CRUD_add(lista, nuevoElemento):
    return lista + [nuevoElemento]

#Version NO PURA
def CRUD_add_impura(lista, nuevoElemento):
    lista = lista + [nuevoElemento]
    return lista

# FUNCION PURA CON DICCIONARIO:
def CRUD_update_diccionario(diccionario, clave, nuevoValor):
    nuevo_diccionario = diccionario.copy() #Copia para que se conserve pura
    nuevo_diccionario[clave] = nuevoValor
    return nuevo_diccionario

print(f"Lista original: {Lista_nombre}")
print(f"Lista nueva: {CRUD_add(Lista_nombre, 'Rosa')}")
print(f"Lista NO PURA: {CRUD_add_impura(Lista_nombre, 'Rosa')}")

#Crendo el diccionario
dic_bd = { "Nombre": "Diego", 
          "Edad": 23, 
          "Estatura": 1.60,
          "Peso": 62.0
        }

print(f"Datos originales: {dic_bd}")
print(f"Datos actualizados: {CRUD_update_diccionario(dic_bd, 'Nombre', 'Mariana')}")
print(f"Datos originales: {dic_bd}")

#FUNCIONES DE ORDEN SUPERIOR
#SON FUNCIONES QUE:
#RECIBEN OTRAS FUNCIONES COMO ARGUMENTOS
#DEVUELVEN FUNCIONES COMO RESULTADOS

# a) Funcion que recibe otra funcion como argumento

def aplicar_funcion(funcion, valorx, valory):
    return funcion(valorx, valory)

print(f"Aplicar funcion suma: {aplicar_funcion(lambda x, y: x + y, 89,63 )}")
print(f"Aplicar funcion resta: {aplicar_funcion(lambda x, y: x - y, 89,63 )}")
#print(f"Aplicar funcion multiplicar: {aplicar_funcion(lambda x, y: x * y, 89,63 )}")
#print(f"Aplicar funcion dividir: {aplicar_funcion(lambda x, y: x / y, 89,63 )}")

# b) Una funcion que devuelve otra funcion
def multiplicador(factor):
    def f(x):
        return x * factor
    return f

duplicar = multiplicador(2) #Duplicar es una funcion 
triplicar = multiplicador(3) #Triplicar es una funcion 

print(f"Doble de 88: {duplicar(88)}")
print(f"Triple de 88: {triplicar(88)}")
 
#MAP

#FILTER

#REDUCE