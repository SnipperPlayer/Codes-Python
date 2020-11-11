#Emmanuel Galeana
#19/10/2020
#Examen 2
def modificar_lista ():
    lista = []
    num = int(input("Numero de elementos: "))
    for i in range(0, num):
        elemento = int(input())
        lista.append(elemento)
        for c in lista:
            if c%2!=0:
                lista.remove(c)

    lista = list(dict.fromkeys(lista))
    lista.sort(reverse = True)
    print(lista)
    
def reemplazar (num):
    lista = []
    for i in range(num):
        texto = input('Dame la palabra: ')
        lista.append(texto)
        lista.append(texto.replace('A', '#').replace('E', '&').replace('I', '+').replace('O', '*').replace('U', '/').replace('a', '#').replace('e', '&').replace('i', '+').replace('o', '*').replace('u', '/')) 
        lista.append('\n')
    print('>'.join(lista))
    
        
def main ():
    opcion = 1
    while opcion != 0:
        opcion = int(input('\nEmmanuel Antonio Galeana González - A01424645\n'+ '19/10/2020\n' + 'TC1028.4\n' + 'Examen final integrador\n' ' \n' + 'Menú \n' + '0. Salir \n' + '1. Modificar lista \n' + '2. Remplazar vocales\n'))
        if opcion == 1:
            modificar_lista()
        elif opcion == 2:
            num = int(input())
            if num > 0:
                reemplazar(num)
            else:
                print('Introduce un numero positivo arriba de 0')
        else:
            if opcion == 0:
                print ('Adios')
                break
    
    
main()