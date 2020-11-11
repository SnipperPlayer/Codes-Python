#Emmanuel Galeana
#21/09/2020
#Separa un string con guiones cada n caracteres

string = input()
numero = int(input())

if numero > 0:
    k = 0
    a ='-'.join([string[k:k+numero]for k in range(0,len(string),numero)])
    print(a)
    
else:
    print('Error')