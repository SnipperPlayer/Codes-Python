#Emmanuel Galeana
#06/09/2020
#Escribe un programa que lea un número entero positivo y que muestre en la pantalla la cantidad de dígitos que tiene.

num = int(input())
resul=0

while num >=1:
    num = num//10
    resul=resul+1
print(resul)
    