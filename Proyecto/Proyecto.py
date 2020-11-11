#Emmanuel Galeana
#11/10/2020


def nuevoContacto():
    contacto = input('Nombre del contacto: ')
    telefono = input('Número telefónico: ')
    correo = input('Correo electrónico: ')
    cumpleanos = input('Fecha de cumpleaños(dia/mes): ')
    lista = []
    lista.append(contacto)
    lista.append(telefono)
    lista.append(correo)
    lista.append(cumpleanos)
    archivo1 = open('archivoContactos.txt', 'a+')
    for i in lista:
        archivo1.write(i)
        archivo1.write('\n')
    archivo1.write('\n')
    archivo1.close()
    
    print("\n{}\n{}\n{}\n{}\n".format(contacto,telefono,correo, cumpleanos))

def borrarContactos():
    archivo2 = open('archivoContactos.txt','r+')  # modo lectura con escritura, puntero al principio por defecto
    contenido = archivo2.read() # leemos todas las líneas
    print(contenido)
    con =  int(input('Ingresa numero de elemento a editar: '))
    entradas = contenido.split('\n\n')
    entrada = entradas[con]
    texto = entrada.split('\n')
    texto[0] = ' '
    texto[1] = ' '
    texto[2] = ' '
    texto[3] = ' '
    archivo2.seek(0)
    for i in texto:
        archivo2.writelines(i)
        archivo2.writelines('\n')
    archivo2.writelines('\n')
    archivo2.close()
    print('Ha sido borrado el contacto')
    
    archivo2 = open('archivoContactos.txt','r+')  # modo lectura con escritura, puntero al principio por defecto
    contenido = archivo2.read() # leemos todas las líneas
    print(contenido)
    con =  int(input('Ingresa numero de elemento a editar: '))
    entradas = contenido.split('\n\n')
    entrada = entradas[con]
    texto = entrada.split('\n')
    texto[0] = ' '
    texto[1] = ' '
    texto[2] = ' '
    texto[3] = ' '
    lista = []
    del entradas [con]
    for i in texto:
        entradas.append(i)
    archivo2.seek(0)
    for i in entradas:
        archivo2.writelines(i)
        archivo2.writelines('\n')
    archivo2.writelines('\n')
    archivo2.close()
    

def editarContacto():
    archivo2 = open('archivoContactos.txt','r+')  # modo lectura con escritura, puntero al principio por defecto
    contenido = archivo2.read() # leemos todas las líneas
    print(contenido)
    con =  int(input('Ingresa numero de elemento a editar: '))
    entradas = contenido.split('\n\n')
    entradas.pop()
    entrada = entradas[con]
    propiedad = int(input('Posición del numero que desea editar: '))
    valor = input('Ingrese Texto: ')
    texto = entrada.split('\n')
    texto[propiedad] = valor
    del entradas [con]
    texto.append('\n')
    for i in texto:
        entradas.append(i)
    entradas.append('\n')
    archivo2.seek(0)
    for i in entradas:
        archivo2.writelines(i)
        archivo2.writelines('\n')
    archivo2.writelines('\n')
    archivo2.close()
    

def listacontactos():
    contador = 0
    f = open('archivoContactos.txt')
    lines = f.read()
    datos = lines.split('\n\n')
    for dato in datos:
        contacto = dato.split('\n')
        print(contador, ', '.join(contacto))
        contador = contador + 1
    f.close()
    

    
def main ():
    opcion = 1
    while opcion != 0:
        try:
            opcion = int(input('\nAdministrador de contactos \n'+ ' \n' + 'Menú \n' + '0. Salir \n' + '1. Nuevo Contacto \n' + '2. Editar contacto \n' + '3. Lista de contactos \n' + '4. Borrar Contacto \n'))
            if opcion == 1:
                nuevoContacto()
            elif opcion == 2:
                editarContacto()
            elif opcion == 3:
                listacontactos()
            elif opcion == 4:
                borrarContactos()
            else:
                if opcion == 0:
                    print ('Adios')
                    break
                else:
                    print('*Ingrese un número válido*')
        except:
            print('//Ingrese un número válido//')
    
    
main()