#Emmanuel Galeana
#06/09/2020
#Escribe un programa que despliegue la suma de los dígitos de un número entero, el número puede ser positivo o negativo, la suma siempre será positiva.

num=int(input())
    
if num<0:
    num=num*(-1)
    
d = 0
while num>=1 or num<=-1:
    v=num%10
    d = d+v
    num = num//10
        
print(d)


