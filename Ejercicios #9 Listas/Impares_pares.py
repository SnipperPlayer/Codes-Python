#Emmanuel Galeana
#28/09/2020
#Pares_impares

num = input()
lista1 = []
lista2 = []

while True:
    if num != 0:
        suma1 = 0
        suma2 = 0
        for i in num:
            if num%2 == 0:
                lista1.append(num)
                suma1 += 1
            elif num % 2 != 0:
                lista2.append(num)
                suma2 += 1
            
    elif num == '*':
        break


print(lista1)
print(lista2)
            
            
            