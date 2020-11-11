#Emmanuel Galeana
#17/08/2020
#Escribe un programa que determine el largo que debe tener una escalera, la cual se necesita para alcanzar una altura determinada cuando se pone contra una casa.
import math

altura = float(input())
angulo = int(input())
rad=math.radians(angulo)

largo = altura/math.sin(rad)
print(round(largo))

