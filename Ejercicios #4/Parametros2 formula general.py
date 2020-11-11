#Emmanuel Galeana
#24/08/2020
#FORMULA GENERAL PARA ECUCIONES DE 2DO GRADO

import math
def calcula(a,b,dis):
    #Resultado de la formula
    if dis == 0:
        resp1 =(-b)/(2*a)
        print(resp1)
    else:
        resp1 = (-b-(math.sqrt(dis)))/(2*a)
        resp2 = (-b+(math.sqrt(dis)))/(2*a)
        print(resp1,resp2)
    
def discriminante(a,b,c):
    #calcula el discriminante
    dis = b**2-4*a*c
    if dis < 0:
        print("respuesta imaginaria")
        return-1
    else:
        calcula(a,b,dis)

def valida_numeros():
    a = float(input("entra tu valor de a: "))
    if a == 0:
        print("a no puede ser 0")
        return valida_numeros()
    else:
        b = float(input("entra tu valor de b "))
        c = float(input("entra tu valor de c "))
        return a,b,c

a,b,c = valida_numeros()
discriminante(a,b,c)