#Emmanuel Galeana, Josue Bahena
#28/08/2020
# Multiplicacion rusa


#Emmanuel Galeana, Josue Bahena
#28/08/2020
# Multiplicacion rusa

a = int(input())
b = int(input())
ans = 0

while a>0:
    print(a,b)
    if(a%2==0):
        b=b*2
        a=a//2
    else:
        ans= ans+b
        b=b*2
        a=a//2
print('resultado='+ str(ans))


