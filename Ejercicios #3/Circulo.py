#Emmanuel Galeana
#20/08/2020
#Escriba un programa que pida el radio y las coordenadas del centro de una circunferencia, así como las coordenadas de un punto.

import math
radio = float(input())
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

perimetro = (math.pi*2*radio)
distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

if y2> radio + y1 :
    print('FUERA')
elif y2< radio + y1:
    print('DENTRO')
elif y2==radio:
    print('SOBRE')
