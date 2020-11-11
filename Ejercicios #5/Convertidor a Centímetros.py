#Emmanuel Galeana
#02/09/2020
#Escribe un programa que convierta pies, pulgadas y yardas a centímetros

def pies(x):
    x=int(input())
    resul=x*30.48
    print(resul)

def pulgadas(y):
    y=int(input())
    res=y*2.54
    print(res)
    
def yardas (z):
    z=int(input())
    resu=z*91.44
    print(resu)
    
def main ():
    opcion = int(input("1 – pies a cm\n"+"2 - pulgadas a cm\n"+"3 – yardas a cm\n"))
    if opcion == 1:
        pies(x)
    if opcion == 2:
        pulgadas(y)
    if opcion == 3:
        yardas(z)
    else:
        print('Error')

main()