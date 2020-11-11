#Emmanuel Galeana
#09/09/2020
#Escribe un programa que lea la clave del artículo que va a comprar (nota que es letra mayúscula) o X si ya no quiere comprar más artículos.


def valor():
    contador = 0
    suma = 0
    num = 0
    g = 0
    h = 0
    j = 0
    while num >= 0:
        try:
            num=int(input())
        except:
            print('dato malo')
            break
        if num >= 200:
            suma += num + g + h + j
            contador += 1
        elif num == 2:
            g = 120
        elif num == 3:
            h = 250
        elif num == 4:
            j = 360
    if contador > 0:
        print(suma)
        
  
if __name__=='__main__':
    valor()