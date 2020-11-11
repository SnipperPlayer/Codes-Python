#Emmanuel Galeana
#17/08/2020
#Escribe un programa que pida al usuario los valores a, b y c y calcule y muestre el área del triángulo usando la fórmula de Helón.

import math
a = float(input())
b = float(input())
c = float(input())

s = ((a + b + c)/2)
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("{0:.3f}" .format(area))