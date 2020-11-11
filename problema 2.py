#Carlos Rodrigo Sánchez Sierra

def problema_2():
    while True:
        try:
            n=int(input("Escribe el dato: "))
        except:
            print("Dije un número >:C")
        else:
            if n>0 and n<100:
                print("Bien hecho :D")
                break
            else:
                print ("No entra en rango")
    termino=0
    serie=0
    a=1
    d=3
    for i in range (1,(n+1)):
        termino=a+(i-1)*d
        print(termino)
        serie=serie+termino
    return(serie)
#a=1 d=3
#𝑎+(𝑛−1)𝑑]
#𝑎+(𝑎𝑎+𝑑𝑑)+(𝑎𝑎+ 2𝑑𝑑)+(𝑎𝑎+ 3𝑑𝑑)+⋯+ [(𝑎𝑎+(𝑛𝑛−1)𝑑𝑑]
suma=problema_2() #O print(problema_2())
print (suma)