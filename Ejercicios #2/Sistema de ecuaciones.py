#Sistemas de ecuaciones con regla de cramer

a11 = float(input("a11: "))
a12 = float(input("a12: "))
c1 = float(input("c1: "))
a21 = float(input("a21: "))
a22 = float(input("a22: "))
c2 = float(input("c2: "))

x = (c1*a22 - a12*c2)/(a11*a22 - a12*a21)
y = (a11*c2 - c1*a21)/(a11*a22 - a12*a21)

print("solucion para x: ",x)
print("solucion para y: ",y)

# MLBC
# 15 08 2020
# Regla Cramer para resolver conjunto de ecuaciones lineales


a11=float(input())
a12=float(input())
c1=float(input())
a21=float(input())
a22=float(input())
c2=float(input())


x1=(c1*a22-c2*a12)/(a11*a22-a12*a21)

x2=(c2*a11-c1*a21)/(a11*a22-a12*a21)


print(x1)
print(x2)
