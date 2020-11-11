def main():
    while True:
        print ("Carlos Rodrigo Sánchez Sierra")
        print ()
        print ("Menú")
        print ()
        print ("   0. Salir")
        print ("   1. Problema 1")
        print ("   2. Problema 2")
        print ("   3. Problema 3")
        print ()
        escoje=int(input("Selecciona una opción: "))
        if escoje==0:
            print ("Gracias por usar el programa")
            break
        elif escoje==1:
            prob_1()
        elif escoje==2:
            num_cant=int(input("Seleccione la cantidad de números a mostrar: "))
            prob_2(num_cant)
        elif escoje==3:
            num_cant=int(input("Seleccione la cantidad de números a mostrar: "))
            prob_3(num_cant)
        else:
            print ("Por favor seleccione una opción válida '0, 1, 2, 3'")
            continue

def prob_1():
    print("-"*66)
    print("|",end=" ")
    print("Año",end=" ")
    print("|",end="")
    print("Depreciación",end="")
    print("|",end="")
    print("Valor al final del año",end="")
    print("|",end="")
    print("Depreciación acumulada",end="")
    print("|")
    for i in range(7):
        x=24000-(4000*i)
        r=int(len(str(x)))
        y=4000*(i+1)
        t=len(str(y))
        print("-"*66)
        print("|",end="  ")
        print(str(i),end="  ")
        print("|",end="    ")
        print("4000",end="    ")
        print("|",end="         ")
        if r==5:
            print(x,end="        ")
        elif r==4:
            print(x,end="         ")
        else:
            print(x,end="            ")
        print("|",end="        ")
        if t==4:
            print(y,end="          ")
        else:
            print(y,end="         ")
        print("|")
    print("-"*66)

def prob_2(x):
    n=1
    sum=0
    while n<(x+1):
        r=(1+(n-1)*3)
        print (r)
        sum=sum+r
        n=n+1
    print ("Serie="+str(sum))

def prob_3(x):
    g=7
    contador = 4
    if x%2==0:
        for i in range(0,int(x/2)):
            if i == ((x/2)-1):
                print (g,",",end="")
                g=g+2
                print (g)
                g=g+4
                contador = 1 + contador
            else:
                print (g,",",end="")
                g=g+2
                print (g)
                g=g+4
                contador = 1 + contador
    else:
        print(g,",",end="")
        for i in range(0,int((x-1)/2)):
            if i ==(int(((x-1)/2)-1)):
                print (g,",",end="")
                g=g+2
                print (g)
                g=g+4
                contador = 1 + contador
            else:
                print (g,",",end="")
                g=g+2
                print (g)
                g=g+4
                contador = 1 + contador

main()
