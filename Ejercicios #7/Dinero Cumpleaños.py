#Emmanuel Galeana
#06/09/2020
#Los padres de un niño le regalarán $10 cuando cumpla n años, y cada cumpleaños doblarán la cantidad que le darán hasta que el obsequio exceda $1000.

edad = int(input())
x=0
j=10

while x<=1000:
    j=j*2
    x=j
    edad=edad+1
    
print(edad,x)
