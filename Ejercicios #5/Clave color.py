#Emmanuel Galeana
#04/09/2020
#Diseña e implementa un programa que transforme una clave en un color.

x = int(input())
def clave_color(x):
    if x==1:
        return('ROJO')
    elif x==2:
        return('AZUL')
    elif x==3:
        return('BLANCO')
    elif x==4:
        return('NEGRO')
    elif x==5:
        return('AMARILLO')
    else:
        return('ERROR')

print(clave_color(x))
        
   
    