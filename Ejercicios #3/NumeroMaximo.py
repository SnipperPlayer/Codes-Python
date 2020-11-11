#Emmanuel Galeana
#20/08/2020
#Realiza un programa que muestre el mayor de 3 números enteros x, y, z proporcionados por el usuario.

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2:
    if num1>=num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>=num3:
        print(num2)
    else:
        print(num3)
