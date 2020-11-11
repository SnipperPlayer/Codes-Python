#Emmanuel Galeana
#10/09/2020
#Primer examen

def convierte_C_a_K(valori,numero,incremento): 
    centigrados = valori
    x = 0
    print('\t # |  centigrados  |  Kelvin   |\t')
    for i in range(numero):
        kelvin = centigrados + 273.15
        x = x+1
        print("\t|{:>2}|\t{:>11.3f}|\t{:>4.3f}|\t".format(x,centigrados,kelvin))
        centigrados=incremento+centigrados


def serie_secuencia (num):
    x=7
    i= 0
    contador=4
    if num>1:
        if num%2 != 0:
            print(x, end=' ')
            for i in range ((num//2)): 
                x=x+2
                b=x+contador
                contador+=1
                print(x,b ,end=' ')
                x=b
        elif num%2 == 0:
            print(x, end=' ')
            for i in range ((num//2)): 
                x=x+2
                b=x+contador
                contador+=1
                print(x,b ,end=' ')
                x=b         
                

def main ():
    opcion = 1
    while opcion != 0:
        opcion = int(input('\nExamen de Emmanuel \n'+ ' \n' + 'Menú \n' + '0. Salir \n' + '1. convierte_C_a_K \n' + '2. serie_secuencia \n'))
        if opcion == 1:
            valori = float(input('Valor inicial de los grados centrigrados a convertir: '))
            numero = int(input('Numero n de conversiones que se haran: '))
            incremento = float(input('Incremento entre los valores centigrados: '))
            convierte_C_a_K(valori,numero,incremento)
        elif opcion == 2:
            num = int(input('Ingresa rango: '))       
            serie_secuencia(num)
        else:
            if opcion == 0:
                print ('Adios')
                break
    
    
main()