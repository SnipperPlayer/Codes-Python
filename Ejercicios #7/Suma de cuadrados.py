#Emmanuel Galeana
#06/09/2020
#Escribe un programa que reciba un número entero y calcule la suma: 12 + 22 + 32 +...+"numero2"

n= int(input())
x=0
y=0

if n >= 0:
    for i in range(1,n+1):
        x = x+1
        y = (x**2) + y
    print(y)
else:
    print(0)