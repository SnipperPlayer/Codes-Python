#Emmanuel Galeana
# 29/09/2020
#Sin duplicados

num = int(input())
lista = []


if num <= 0:
    print('Error')
else:
    for i in range (num):
        string = input()
        lista.append(string)
        
    lista1 = []    
    for i in lista:
        if i in lista1:
            continue
        else:
            lista1.append(i)
            
    print(lista)
    print(lista1)

    