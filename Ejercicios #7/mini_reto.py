#Miguel Jiménez, Emmanuel Galeana, Gabdiel Adame
#31/08/2020
#Pintar y mcd


def pide_numeros():
    print('Ingrese un número Entero Positivo')
    n1=-1
    n2=-1
    while n1<=0 and n2<=0:
        
        try:
            x=int(input('n1: '))
            y=int(input('n2: '))
            
            if x>0 and y>0: 
                n1=x
                n2=y
        except:
            print('Error: porfavor, ingrese un número válido (Entero Positivo)')
           
                
                
        if n1<=0 or n2<=0:
            print('Porfavor, ingrese un número válido (Entero Positivo)')
        else:
            return (n1,n2)
            
    
def mcd(a,b):
    
    cont=0
    
    if a%b==0:
        print('El mcd es: ' ,b) 
    elif b%a==0:
        print('El mcd es: ' ,a) 
    
    
        
    for i in range (1, a+1):
        if a%i==0 and b%i==0:
            cont=i
    print(cont)




def pide_caracter():
    
    c='0'
    while c!='*' and c!='=' and c!='+':
        c=input('Ingrese uno de los siguientes caractéres: * + = ')
        if c!='*' and c!='=' and c!='+':
            print('caracter inválido, ingrese nuevamente: ')
        
    return c
    
         

def pinta_figura(c):
    x=0
    
    for i in range (10,0,-1):
        
        print(c*(10-x),(x+1)*' ', c*(x+1),(20-(x*2))*' ',c*(x+1),(x+1)*' ',c*(10-x)) 
        x=x+1
            
    
    
def main():
    
    opcion=0
    while opcion!=3:
        try:
            opcion=int(input('elija una de las siguientes opciones: \n'+'1: Mínimo común divisor \n'+ '2: Pinta figura \n' + '3: Salir \n'))
        except:
            print('Error')
        else:
            
            if opcion==1:
                a,b=pide_numeros()
                mcd(a,b)
        
        
            elif opcion==2:
                c=pide_caracter()
                pinta_figura(c)
                
        
main()






