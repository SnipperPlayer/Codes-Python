#Emmanuel Galeana
#04/10/2020
#Suma columnas de una matriz

def genera_matriz (ren, col):
    matriz = []
    lista=[]
    for i in range(ren):
        lista=[]
        for i in range (col):
            lista.append(int(input()))
        matriz.append(lista)    
    
    return matriz
    

def suma_columnas (matriz,renglon,columna):
    
    
    lista= []
    c=[]
    countx=[]
    
    for h in range(columna):
        c=[]
        for j in range (renglon):
            for k in range (columna):
                if h==k:
                    c.append(matriz[j][k])
        c=sum(c)
        lista.append(c)
    
    return lista


def main():
    ren = int(input())
    col = int(input())
    if ren<1 or col<1:
        print('Error')
    else:
        y=genera_matriz(ren,col)
        print(suma_columnas(y,ren,col))

main()