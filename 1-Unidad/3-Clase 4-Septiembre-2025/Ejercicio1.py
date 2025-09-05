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

#COMO LO HACEMOS CON UN CICLO?
#PIDEMOS PRIMERO LOS 100

data_gmail = []
data_hotmail = []
 
for i in range(100):
    try:
        data = next(fuente_datos) # Pedir datos de forma perezosa:
        #Filtra y agrega a la lista de hotmail o a la de gmail. 
        if "gmail" in data: 
            data_gmail.append(data)
    except StopIteration:
        print("El generador no puede generar más datos.")        

#HACERLO CON OTROS 100 DATOS
for i in range(100):
    try:
        data = next(fuente_datos) # Pedir datos de forma perezosa:
        #Filtra y agrega a la lista de hotmail o a la de gmail. 
        if "hotmail" in data: 
            data_hotmail.append(data)
    except StopIteration:
        print("El generador no puede generar más datos.")

#Imprimiendo resultados
print("---------RESULTADOS---------")
print("Gmail:", data_gmail)
print("\nHotmail:", data_hotmail)