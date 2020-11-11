#Gabdiel Adame, Emmanuel Galeana, Ian Doring
#01/10/2020
#Mini reto matrices

from random import randint


def matriz(renglon, columna):
    return [ [randint(0,100) for c in range(columna)] for r in range(renglon)]


def grado():
    grado = 0
    renglon = grado
    columna = grado
    while grado < 2:
        try:
            grado = int(input("Elige el grado: "))
            if grado < 2:
                print("Numero debe ser mayor o igual a 1")       
        except:
            print("Numero debe ser mayor o igual a 1")
    return grado

def imprime(matriz):
    for elemento in matriz:
        print (elemento)
    
def imprime_L(matriz, grado):
    matriz_L = []
    for r in range (grado):
        linea_c = []
        for c in range (grado):
            if c == 0 or r == grado-1:
                linea_c.append(matriz[r][c])
        matriz_L.append(linea_c)
    return matriz_L

def imprime_E(matriz, grado):
    matriz_E = []
    mitad = grado//2
    for r in range (grado):
        linea_c = []
        for c in range (grado):
            if c == 0 or r == 0 or r == mitad or r == grado-1:
                linea_c.append(matriz[r][c])
        matriz_E.append(linea_c)
    return matriz_E
    
def imprime_X(matriz, grado):
    matriz_X = []
    grado1=grado-1
    for r in range (grado):
        linea_c = []
        for c in range (grado):
            if c == r or c == grado1:
                linea_c.append(matriz[r][c])
            else:
                linea_c.append('')
                
        grado1 = grado1-1
            
                
        matriz_X.append(linea_c)
    return matriz_X
    
def elige_letra():
    letra = input("Elige una letra E, L, X: ")
    if letra == "X":
        renglon = grado()
        columna = grado()
        matriz_de_X = imprime_X(matriz(renglon, columna), renglon)
        imprime(matriz_de_X)
        
    elif letra == "E":
        renglon = grado()
        columna = grado()
        matriz_de_E = imprime_E(matriz(renglon, columna), renglon)
        imprime(matriz_de_E)
        
    elif letra == "L":
        renglon = grado()
        columna = grado()
        matriz_de_L = imprime_L(matriz(renglon, columna), renglon)
        imprime(matriz_de_L)
        
        
        
elige_letra()
 