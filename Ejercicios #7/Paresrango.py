#Emmanuel Galeana
#04/09/2020
#Pares dentro de un rango

x=int(input())
y=int(input())

def rango_pares(num1,num2):
    for i in range(num1, num2+1):
        if i%2 ==0:
            print(i)
rango_pares(x,y)