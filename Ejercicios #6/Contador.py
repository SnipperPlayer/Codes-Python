#Emmanuel Galeana
#27/08/2020
#Contador

def valor():
    contador = 0
    suma = 0
    num = 0
    while num >= 0:
        try:
            num=int(input())
        except:
            print('dato malo')
            break # / continue
        if num >= 0:
            suma += num
            contador += 1
    if contador > 0:
        print('suma: ',suma)
        print('promedio: ',suma/contador)
  
if __name__=='__main__':
    valor()