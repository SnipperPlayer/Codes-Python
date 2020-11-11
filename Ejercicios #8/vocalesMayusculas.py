#Emmanuel Galeana
#21/09/2020
#Vocales a mayúsculas

string = input()

a = ''.join(['#' if c in ['a', 'e', 'i', 'o', 'u'] else c for c in string])
b = ''.join(['&' if c in ['e'] else c for c in string])
c = ''.join(['+' if c in ['i'] else c for c in string])
d = ''.join(['*' if c in ['o'] else c for c in string])
e = ''.join(['/' if c in ['u'] else c for c in string])

print(a,b,c,d,e)