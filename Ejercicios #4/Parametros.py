#Emmanuel Galeana
#24/08/2020
#Dame un rango y un numero, y te dire si esta en el rango o no

def validar(num1, num2):
    val1 = int(input())
    if val1 >= num1 and val1 <= num2:
        num = val1
    else:
        num = -1
    return(num)

F = validar(int(input()), (int(input())))
print(F)

    
    