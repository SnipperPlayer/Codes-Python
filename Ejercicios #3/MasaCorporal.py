#Emmanuel Galeana
#20/08/2020
#Escribe un programa que calcule el IMC (Indice de Masa Corporal) de una persona.

peso = float(input())
altura = float(input())

indice = peso/(altura**2)

if indice < 20:
    print('PESO BAJO')
elif indice >=20 and indice < 25:
    print('NORMAL')
elif indice >= 25 and indice < 30:
    print('SOBREPESO')
elif indice >= 30 and indice < 40:
    print('OBESIDAD')
elif indice >= 40:
    print('OBESIDAD MORBIDA')