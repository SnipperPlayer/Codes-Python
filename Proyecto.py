#Emmanuel Galeana
#11/10/2020


def nuevoContacto(contacto, telefono, correo, cumpleanos):
    lista = []
    lista.append(contacto)
    lista.append(telefono)
    lista.append(correo)
    lista.append(cumpleanos)
    print("\n{}\n{}\n{}\n{}\n".format(contacto,telefono,correo, cumpleanos))


def editarContacto(nombre):
    buscar = nombre
    print('i') 
    
    
def listacontactos():
    print(2)
    
    
    
def main ():
    opcion = 1
    while opcion != 0:
        opcion = int(input('\nAdministrador de contactos \n'+ ' \n' + 'Menú \n' + '0. Salir \n' + '1. Nuevo Contacto \n' + '2. Editar contacto \n' + '3. Lista de contactos \n'))
        if opcion == 1:
            contacto = input('Nombre del contacto: ')
            telefono = int(input('Número telefónico: '))
            correo = input('Correo electrónico: ')
            cumpleanos = input('Fecha de cumpleaños(dia/mes): ')
            nuevoContacto(contacto, telefono, correo, cumpleanos)
        elif opcion == 2:
            nombre = input('Nombre del contacto que quiere edita: ')
            editarContacto(nombre)
        elif opcion == 3:
            listacontactos()
        else:
            if opcion == 0:
                print ('Adios')
                break
    
    
main()