#Emmanuel Galeana
#06/09/2020
#Escribe un programa que reciba un entero y devuelva True si es un número primo y False si NO es un número primo.

numero = int(input())
numero = abs(numero)
if numero == 1:
    print("False")
elif numero % 2 != 0:
    print("True")
elif numero == 2:
    print("True")
else:
    print("False")