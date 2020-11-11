
def uno():
    dato = input()
    n= 0
    for i in range (10,0,-1):
        print(dato*(10-n)," "*(n+1))#, dato*(n+1) , " "*(20-(n*2)),dato*(n+1)," "*(n+1),dato*(10-n),  sep="")  
        n= n +1



uno()
