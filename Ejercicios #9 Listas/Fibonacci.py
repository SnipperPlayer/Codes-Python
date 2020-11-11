#Emmanuel Galeana
#29/09/2020
#Serie de fibonacci en una lista

num = -1
lista=[]
while num < 0:
    num=int(input())
    x=0
    y=1
    z=0
    for i in range(num):
        x=y
        y=z
        lista.append(z)
        z=x+y

print(lista)


