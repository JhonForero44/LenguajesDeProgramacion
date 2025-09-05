#Lazy evaluation: Las expresiones no se calculan inmediatamente.
#Concepto:

#Lo opuesto: "eager" evaluation

#1. Eager Evaluation: Evaluacion inmediata: un de la data de 100000 usuarios: 
usuarios = []
for i in range(100000):
    if i % 3 == 0:
        usuarios.append(f"user{i}@gmail.com")
    else:
        usuarios.append(f"user{i}@hotmail.com")

#Filtrar usuarios con cuenta gmail
usuarios_gmail = []
for u in usuarios:
    if "gmail" in u: #El gmail es del dominio gmail
        usuarios_gmail.append(u)

#Imprimir los primeros 5 (procesar lotes de 5)
print("---------GENERAR Y CONSUMIR DATOS---------")
print(usuarios_gmail[:5])

#2. Lazy Evaluation: Evaluacion perezosa:Produce los 100000 usuarios uno a la vez, solo cuando se necesitan.

#FUNCION GENERADORA PEREZOSA
#PRODUCTO PEREZOSO
def generar_usuarios_data():
    for i in range(500000000):
        if i % 3 == 0:
            #YIELD GENERA EL VALOR, SI LO PIDE, Y PAUSA EL CICLO HASTA EL SIGUIENTE PASO
            yield f"User{i}@gmail.com"
        else:
            yield f"User{i}@hotmail.com"
            
# CONSUMIDOR PEREZOSO
# Asignamos la funcion del producto perezoso a una variable
fuente_datos = generar_usuarios_data()

print("---------GENERAR Y CONSUMIR DATOS PEREZOSAMENTE---------")
#Consumir los datos de uno en uno, con el next
primer_dato = next(fuente_datos)
print(primer_dato)
segundo_dato = next(fuente_datos)
print(segundo_dato)
tercer_dato = next(fuente_datos)
print(tercer_dato)
cuarto_dato = next(fuente_datos)
print(cuarto_dato)