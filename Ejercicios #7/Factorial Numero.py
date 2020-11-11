#Emmanue Galeana
#06/09/2020
#Calcular el factorial de un número N, donde N es solicitado al usuario.

num= int(input())
cont = 1
t = 1
if num < 0:
    print("Factorial no definido para negativos")
elif (num == 0 or num == 1):
    print("1")
else:
    while cont <= num:
        t = t * cont
        cont = cont +1
    print (t)

