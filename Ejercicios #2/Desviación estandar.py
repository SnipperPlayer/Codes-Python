#Emmanuel Galeana
#17/07/2020
#escribe un programa que calcule y muestre la desviación estándar de 5 números proporcionados por el usuario.

import math
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

prom = (n1+n2+n3+n4+n5)/5
m1=(n1-prom)**2
m2=(n2-prom)**2
m3=(n3-prom)**2
m4=(n4-prom)**2
m5=(n5-prom)**2

suma=(m1+m2+m3+m4+m5)
div= suma/5
raiz=math.sqrt(div)
print(raiz)