#Emmanuel Galeana
#28/09/2020

from random import randint


grado = 0
renglon = grado
columna = grado
while grado <= 0:
    try:
        grado = int(input())
        if grado <= 0:
            print("Numero debe ser mayor o igual a 1")       
    except:
        print("Numero debe ser mayor o igual a 1")

def matriz1(grado, grado):
    matriz1 =[ [randint(0,100) for c in range(columna)] for r in range(renglon)]
    return matriz1


letra = 0
while letra != 'X' and letra != 'E' and letra != 'L':
    try:
        letra = input()
        if letra != 'X' and letra != 'E' and letra != 'L':
            print("Letra debe ser X, E, L")
            
    except:
        print("Letra debe ser X, E, L")

def matrizL(matriz1):
    if letra == "X":
        matriz = []
        num = randint(0, 100)
        for r in range(grado):
            renglon = []
            for c in range(grado):
                renglon.append(num)
                num = randint(0, 100)
            matriz.append(renglon)
        print(matriz[0][0],"''", matriz[0][2])
        print("''", matriz[1][2], "''")
        print(matriz[2][0],"''", matriz[2][2])

    
    elif letra == "E": 
        matriz = []
        num = randint(0, 100)
        for r in range(grado):
            renglon = []
            for c in range(grado):
                renglon.append(num)
                num = randint(0, 100)
            matriz.append(renglon)
        print(matriz[0][0],"''", matriz[0][2])
    
    elif letra == 'L':
        matrizN=[]
        for ndx, mat in enumerate(matriz1):
            if ndx==len(mat)-1:
                matrizN.append(mat)
            else:
                matrizN.append(([mat[0]]) + (len(mat)-1)*[''])
        print(matrizN)

matrizL(matriz1)
            
