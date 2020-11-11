#Emmanuel Galeana
#04/10/2020
#Centro de matriz

x = int(input())
y = int(input())
def matriz(renglon,columna):
    matriz = []
    for r in range(renglon):
        renglon = []
        for c in range(columna):
            num=int(input())
            renglon.append(num)
        matriz.append(renglon)
        
    try:
        matriz.pop(0)
        matriz.pop(-1)
    except:
        pass
    
    for x in range (len(matriz)):
        try:
            matriz[i].pop(0)
            matriz[i].pop(-1)
        except:
            pass
    print(matriz[0][0])
    
matriz(x,y)