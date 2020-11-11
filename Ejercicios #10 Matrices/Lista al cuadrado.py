#Emmanuel Galeana
#04/10/2020
#Lista al cuadrado

def matriz(renglon,columna):
    matriz = []
    for r in range(renglon):
        renglon = []
        for c in range(columna):
            num=int(input())
            renglon.append(num)
        matriz.append(renglon)
        
    
    lista = []
    for x in matriz: # aqui estas pasando por todas las filas de la matriz
        contador = 0
        for i in x: # aqui estas pasando por todos los elementos de esta fila
            if i % 2 ==0:
                contador += 1
        lista.append(contador)
    print(lista)

x = int(input())
y = int(input())
matriz(x,y)