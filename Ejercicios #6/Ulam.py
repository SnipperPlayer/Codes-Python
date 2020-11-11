#Emmanuel Galeana, Josue Bahena
#28/08/2020
#Conjetura de Ulam

user = int(input())

def collatz(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n=n//2
            print(n)
        else:
            n = n*3+1
            print(n)
            
collatz(user)