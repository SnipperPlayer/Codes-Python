#Emmanuel Galeana
#28/09/2020
#Listas


lista=[1,'hola',['elemento en 2da lista', '50']]
pos=0


print(lista[2][1])

for elemento in lista:            #Para devolver la lista con su index o posición
    print(pos,",",elemento)
    pos+=1
