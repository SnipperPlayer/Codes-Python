#mFunción que crea una matriz de enteros consecutivos de nxm columnas
from random import randint

def crea_matriz(renglon,columna):
# funcion que construye una matriz de renglon x columna elementos consecutivos
    matriz = []
    num = 1
    for r in range(renglon):
        renglon = []
        for c in range(columna):
            renglon.append(num)
            num += 1
        matriz.append(renglon)
    return matriz

def crea_matriz2(renglon, columna):
# funcion que construye una matriz de renglon x columna elementos aleatorios
    return [ [randint(0,50) for c in range(columna)] for r in range(renglon)]
              
def valida_parametro(minimo, letrero):
# funcion que valida un numero a partir de un valor minimo
# ENTRADA: minimo, establece el minimo valido a aceptar
#          letrero, es lo que se desea imprimir
    while True:
        try:
            numero = int(input(letrero))
        except:
            print("Debes introducir un número, intenta de nuevo")
        else:
            if numero >= minimo:
                break;
            else:
                print("Debes introducir valores mayores o iguales a 2")
    return numero
        
def main():
    print("\nMatriz con numeros consecutivos\n")
    ren = valida_parametro(2, "Número de renglones: ")
    col = valida_parametro(2, "Número de columnas: ")
    print("\nMatriz\n",crea_matriz(ren,col))
    
    print("\nMatriz con numeros aleatorios\n")
    print(crea_matriz2(valida_parametro(2, "Número de renglones: "),valida_parametro(2, "Número de columnas: ")))

main()