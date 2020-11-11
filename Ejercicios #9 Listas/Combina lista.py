#Emmanuel Galeana
#29/09/2020
#Combina Listas

cuenta = 0
d = ""
lista1 = []
lista2 = []
contador1 = 0
contador2 = 0
contador3 = -1
lista3 = []
def fun(cuenta, d, lista1, lista2, contador1, contador2, lista3, contador3):
    t1 = int(input())
    t2 = int(input())
    contador1 = t1
    contador2 = t2
    if t1 <= 0 or t2 <= 0:
        print("Error")
    else:
        print("-----")
        while cuenta != t1:
            d = input()
            lista1.append(d)
            cuenta = cuenta +1
        print("-----")
        cuenta = 0
        while cuenta != t2:
            d = input()
            lista2.append(d)
            cuenta = cuenta +1
        cuenta= 0
        print("-----")
        print(lista1)
        print(lista2)
        
        if t1 < t2:
            while cuenta != t2:
                contador3 = contador3 +1
                if contador1 > 0:
                    lista3.append(lista1[contador3])
                    contador1 = contador1-1
                if contador2 > 0:
                    lista3.append(lista2[contador3])
                    contador2 = contador2-1
                cuenta = cuenta +1
        elif t1 > t2:
            while cuenta != t1:
                contador3 = contador3 +1
                if contador1 > 0:
                    lista3.append(lista1[contador3])
                    contador1 = contador1-1
                if contador2 > 0:
                    lista3.append(lista2[contador3])
                    contador2 = contador2-1
                cuenta = cuenta +1
        else:
            while cuenta != t1:
                contador3 = contador3 +1
                if contador1 > 0:
                    lista3.append(lista1[contador3])
                    contador1 = contador1-1
                if contador2 > 0:
                    lista3.append(lista2[contador3])
                    contador2 = contador2-1
                cuenta = cuenta +1
        print(lista3)
            
            
                
fun(cuenta, d, lista1, lista2, contador1, contador2, lista3, contador3)

