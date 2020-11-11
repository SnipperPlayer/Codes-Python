#Emmanuel Galeana
#13/08/2020

#Mostrar el dato
x = input('Enter dato: ')
print(x)

#Sumar datos
dato1 = int(input('dato 1: '))
dato2 = int(input('dato 2: '))
print(dato1 + dato2)

#Convertir metros a kilometros        
metros = int(input('ingrese dato en metros: '))
kilometros = metros/1000
print('los kilometros son: ' , kilometros)

#Convertir Segundos a horas
segundos = int(input('ingresa dato en segundos: '))
horas = segundos/3600
print('las horas son: ' , horas)

#Saber el iva de algo
precio = float(input("precio: "))
print('iva: ' + str(precio * 0.16))
print('total: ' + str(precio * 1.16))