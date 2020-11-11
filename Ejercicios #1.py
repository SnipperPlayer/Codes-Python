#Emmanuel Galeana
#16/08/2020
#Escribe un programa que lea los datos: base (b) y altura (h) y muestre el área del triángulo.

base = float(input())
altura = float(input())

area = print(float((base * altura)/2))

#Promedio de 4 materias

mat1 = int(input())
mat2 = int(input())
mat3 = int(input())
mat4 = int(input())

prom = print(float((mat1 + mat2 + mat3 + mat4)/4))

#Crea un programa que pregunte al usuario su edad y el año actual, como resultado le indicará el año en que cumplirá 100 años.

edad = int(input())
actual_ano = int(input())

edad2 = print(int((100 - edad) + actual_ano))

#Realiza un programa que indique el número de lustros que ha vivido una persona por medio de su año de nacimiento y el año actual.

nacimiento = int(input())
anoActual = int(input())

lustros = print(float(anoActual - nacimiento)/5)

#Realiza un programa que ayude a las personas a indicar cuántos kilos debe bajar por mes una persona dados el peso inicial, el peso final y el número de meses que una persona estará en un programa integral para bajar de peso.

pesoinicial = float(input())
pesofinal = float(input())
meses = int(input())

bajarKilos = print(float((pesoinicial - pesofinal)/meses))

#Pendiente de una recta

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

m = print(float((y2 - y1)/(x2 - x1)))

#Realiza un programa para indicar cuántos centímetros recorrerá el caracol en una cantidad de minutos dada por el usuario.

minutos = float(input())
conv = minutos*60
conv2 = (5.7/10)*conv

cm = print(float(conv2))

#Realiza un programa que calcule el costo total mensual de un usuario según estos datos.

nmensajes = int(input())
nmegas = float(input())
nminutos = int(input())

costo= print(float((nmensajes + nmegas + nminutos)*0.80))

#Escribe un programa que sirva para calcular el total de la compra de videojuegos.

jnuevos = int(input())
jusados = int(input())
cnuevo = int(jnuevos*1000)
cusados = int(jusados*350)

toTal = print(int(cnuevo + cusados))

#Emmanuel Galeana
#16/08/2020
#Haz un programa sirva para calcular el precio que va a pagar un cliente por comprar cemento.

bultoCemento = int(input())
precioBulto = float(input())
precioTotal = float(bultoCemento * precioBulto)

sinIva = print(float(precioTotal))
conIva= print(float(precioTotal * 0.16))
total = print(float(precioTotal)+(precioTotal * 0.16))


