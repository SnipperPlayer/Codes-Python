#Emmanuel Galeana
#29/09/2020
#Mezcla y ordena listas

lista1=[]
lista2=[]
while True:
    num = input()
    if num=='*':
        break
    else:
        try:
            num=int(num)
            if num>=0:
                lista1.append(num)
        except:
            continue

while True:
    num = input()
    if num=='*':
        break
    else:
        try:
            num=int(num)
            if num>=0:
                lista2.append(num)
        except:
            continue

lista3=[]
lista3.extend(lista1+lista2)
lista3.sort()

print('L1=')
print(lista1)
print('L2=')
print(lista2)
print('LORDENADA=')
print(lista3)
    