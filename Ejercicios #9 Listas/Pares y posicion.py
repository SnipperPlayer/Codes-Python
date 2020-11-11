#Emmanuel Galeana
#29/09/2020
#Pares y posición

num = int(input())
lista=[]
for i in range (num):
    dato = int(input())
    lista.append(dato)

cuenta = -1
for i in lista:
    cuenta += 1
    if i % 2 == 0:
        print('pos', cuenta, ',', 'valor',i)

