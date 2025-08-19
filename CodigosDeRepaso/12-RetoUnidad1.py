##  DATOS PARA REALIZAR LA PRUEBAS
# adulto =  12000
# menores = 10000 
#descuento 1 = 10% si son 2 boletas
#descuento 2 = 15% si son 3 boletas
#descuento 3 = 20% si son 4 boletas

#Creamos la definicion solicitada
def calcularTotalBoletas(cantidad_adultos, cantidad_menores):
# Procedemos a multiplicar el valor de la cantidad de adultos y menores ingresados por el valor de la boleta
    valor_total_adultos = cantidad_adultos*12000
    valor_total_menores = cantidad_menores*10000
#Procedemos a sumar el total de la cantidad de adultos y menores que ingresaron
    totalAsistentes = cantidad_adultos+cantidad_menores
#Usamos la herraminenta "if"
# Si el "totalAsistentes" es igual a 2, entonces se procede a multiplicar por 0.9 que equivale al 10%
#Usamos el "totalAsistentes" para realizar el ejercicio ya que dentro de el contiene la cantidad de adultos y menores ingresados
    if totalAsistentes == 2:
        valor_total_adultos = valor_total_adultos * 0.9
        valor_total_adultos = valor_total_menores * 0.9
#Si el "totalAsistentes" es igual a 2, entonces se procede a multiplicar por 0.85 que equivale al 15%
#Usamos el "totalAsistentes" para realizar el ejercicio ya que dentro de el contiene la cantidad de adultos y menores ingresados
    elif totalAsistentes ==3:
        valor_total_adultos = valor_total_adultos * 0.85
        valor_total_menores = valor_total_menores * 0.85
#Si el "totalAsistentes" es igual a 2, entonces se procede a multiplicar por 0.8 que equivale al 20%
#Usamos el "totalAsistentes" para realizar el ejercicio ya que dentro de el contiene la cantidad de adultos y menores ingresados
    elif totalAsistentes ==4:
        valor_total_adultos = valor_total_adultos * 0.8
        valor_total_menores = valor_total_menores * 0.8
        
#Se procede a realizar la suma del total a pagar por los adultos y del total a pagar por los menores para tener el valor total     
    valor_total = valor_total_adultos + valor_total_menores

#Como lo dice el ejercicio se procede a retornar un mensaje como aparece mas abajo
#Usamos la opcion print para visualizar el mensaje
#Usamos la opcion "str" ya que el ejercicio nos solicita este retorno     
#Y usamos la opcion "int" para pasar los resultados que den flotantes a enteros
    return (f"El valor a pagar por adultos es: {valor_total_adultos} y por menores es: {valor_total_menores} para un total a pagar de: {valor_total}")

#Esta opcion nos sirve para llamar la funcion
#Dentro del parentesis procederemos a colocar los valores que use la funcion	
print(calcularTotalBoletas(0,1))
