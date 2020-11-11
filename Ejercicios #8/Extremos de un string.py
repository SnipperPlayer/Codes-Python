#Emmanuel Galeana
#21/09/2020
#Extremos de un string

stri = input()
strin = len(stri)
if strin > 1:
    print (stri[:2]+stri[-2:])
else:
    print("")