#Emmanuel Galeana
#07/09/2020
def problema1 ():
    x = 28000
    y = 4000
    p=0
    r= 0
    print('\tAño | Deprecion | Valor al final del año | Deprecion acumulada | \t')
    for i in range(7):
        r += 1
        x = x-y
        p = p + y
        print("\t|{:^2}|\t|{:^9}|\t|{:^12}|\t|{:^20}|\t".format(r,y,x,p))


def problema2(numero):
    termino = 0
    serie = 0
    a = 1
    d = 3
    if numero>2:
        for i in range (1,(numero+1)):
            termino = a+(i-1)*d
            print(termino)
            serie = serie + termino
        return(serie)
    else:
        print('Dato invalido, intenta de nuevo')
            
       
def problema3 (num):
    x=3
    i= 0
    if num>4:
        if num%2 == 0 or num%2!=0:
            print('3', end=' ')
        for i in range (num//2): 
            x=x*6
            b=x-4
            print(x,b ,end=' ')
            x=b
    else:
        print('Error')
        
    
def main ():
    opcion = 0
    while opcion != 1:
        opcion = int(input('Examen de Emmanuel \n'+ ' \n' + 'Menú \n' + '0. Salir \n' + '1. Problema 1 \n' + '2. Problema 2 \n' + '3. Problema 3 \n'))
        if opcion == 1:
            problema1()
        elif opcion == 2:
                numero = int(input('ingrese dato: '))
                print(problema2(numero))
        elif opcion == 3:
            num = int(input('Ingresa rango: '))       
            problema3(num)
        else:
            if opcion == 0:
                print ('salida')
                break
    
    
main()


