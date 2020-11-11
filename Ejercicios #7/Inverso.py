#Emmanuel Galeana
#06/09/2020
#Escribe un programa que dado un número, muestre en la pantalla su inverso numérico, es decir un número que tiene los mismos dígitos pero en orden inverso.

num = int(input())
s = ""
cont = 0
t = ""
if num < 0:
    s = "-"
    num = abs(num)
        
while num > 0:
    cont = num%10
    t = str(t) + str(cont)
    num = num //10
if  s != "":
    print(s + t)
else:
    print(t )