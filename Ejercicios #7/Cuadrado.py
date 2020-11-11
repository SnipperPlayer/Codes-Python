#Emmanuel Galeana
#06/09/2020
#Escribe un programa que reciba un número entero y como resultado, debe encontrar el menor número tal que al elevarlo al cuadrado sea mayor que el número N dado por el usuario.

#Emmanuel Galeana
#06/09/2020
#Escribe un programa que despliegue la suma de los dígitos de un número entero, el número puede ser positivo o negativo, la suma siempre será positiva.

num = int(input())
x = 0
contador = 0
while contador <= num:
    x = x + 1
    contador = (x**2)
print(x)