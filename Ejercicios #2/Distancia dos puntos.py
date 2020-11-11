#Emmanuel Galeana
#17/08/2020
#Desarrolla un programa en Python que calcule la distancia entre dos puntos del plano cartesiano.
import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

p1 = float(x2 - x1)**2
p2 = float(y2 - y1)**2
distancia = float(math.sqrt(p1 + p2))
print(("distancia= {0:.2f}".format(distancia)))
