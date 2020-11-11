#Emmanuel Galeana
#17/08/2020
#Escribe un programa en Python que reciba dos entradas: un  y un . El programa debe primero calcular el valor usando la fórmula de arriba. Posteriormente debe multiplicar el resultado anterior por el valor redondeando el resultado  dígitos de precisión después del punto decimal. Finalmente debe imprimir el resultado.

import math
f = float(input())
k = int(input())
raiz = float(math.sqrt(5))
proce = (1 + raiz)/2
op = proce*f
print("{}" .format(round(op ,k)))
