#Emmanuel Galeana
#06/09/2020
#Escribe un programa que lea un valor n y que muestre en la pantalla n caracteres que alternan entre

n = int(input())

for i in range(n):
    if i % 2 == 0:
        print('#')
    elif i != 2:
        i = 2*i+1
        print('%')   
