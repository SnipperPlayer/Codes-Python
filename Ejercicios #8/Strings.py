#Emmanuel Galeana
#21/09/2020
#String


def numeroCadena():             #Para contar cuantos caracteres tiene una cadena
    x = input('Dame una cadena: ')
    print('tu cadena tiene {} caracteres' .format(len(x)))
    
numeroCadena()

def vocales():                  #Para contar las vocales
    s = input('Dame un string: ')
    v = len([c for c in s.lower() if c in ['a', 'e', 'i', 'o', 'u']])
    print('Tu string tiene {} vocales' .format(v))
vocales()

def contar():                   #Para que salga 2 letras del principio y 2 letras de final
    string = input('Dame un string: ')
    cadena = len(string)
    if cadena > 2:
        inicio = (string[:2])
        final = (string[-2:])
        print('{}{}' .format(inicio, final))
    else:
        print('')
        
contar()
    
def cadena():                #Para sustituir un * en letras que se repitan a la primera letra
    stri = input('Dame una cadena: ')
    primer = stri[0]
    segundo = primer.lower()
    otro = stri[1:]
    print(primer + otro.replace(segundo,'*'))
    
cadena()