#Emmanuel Galeana
#20/08/2020
#Escribe un programa que lea un número entero que se encuentre entre 0 y 360 que representa los grados del plano cartesiano y que muestre como resultado el número de cuadrante en donde se encuentra.

grados = int(input())

if grados<0 or grados>360:
    print('excede')
elif grados==0 or grados==90 or grados==180 or grados==270:
    print('eje')
elif grados>0 and grados<90:
    print('cuadrante 1')
elif grados>90 and grados<180:
    print('cuadrante 2')
elif grados>180 and grados<270:
    print('cuadrante 3')
elif grados>270 and grados<360:
    print('cuadrante 4')

    


