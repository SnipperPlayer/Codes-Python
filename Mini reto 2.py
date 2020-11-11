#Emmanuel Galeana
#15/10/2020
#Mini reto

def cmatriz(grado):
    r = grado
    c = grado

    matriz = [ [int(input()) for c in range(c)] for r in range(r)]
    return matriz

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

def transpuesta (cmatriz):
    for i in range(len(cmatriz)):
        for j in range(len(cmatriz)):
                print(cmatriz[j][i], end=' ')   
        print()
        
def texto ():
    texto = "un día que el viento soplaba con fuerza#mira cómo se mueve aquella banderola -dijo un monje#lo que  se  mueve  es  el  viento  -respondió  otro  monje#ni  las  banderolas  ni  el  viento,  lo  que  se  mueve  son vuestras mentes -dijo el maestro "
    a = texto.replace('#','\n - ')
    print(a)
    
    
def main ():
    opcion = 1
    while opcion != 0:
        opcion = int(input('\nEmmanuel Galeana \n' + '\n15/10/2020 \n' + ' \n' + '\nMenú \n' + '0. Salir \n' + '1. Problema 1 \n' + '2. Problema 2 \n' + '\nEl menú debe repetirse mientras el usuario no oprima la opción para salir. Cada problema debe resolverse en una función.\n' + '\nToda petición de datos al usuario, en caso de ser requerida, deberá realizarse en el main y enviar a la función los datos como parámetros.\n' + '\n Todo resultado generado en cada problema que requiera ser desplegado, deberá atender las especificaciones en cada caso. Por favor, atiende este requerimiento.\n'))
        if opcion == 1:
            transpuesta(cmatriz(grado()))
        elif opcion == 2:
            texto()
        else:
            if opcion == 0:
                print ('Adios')
                break
     
main()