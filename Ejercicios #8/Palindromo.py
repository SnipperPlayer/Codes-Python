#Emmanuel Galeana
#21/09/2020
#Palíndromo

pali = input().lower()
pali = "".join([c for c in pali if c != " "])
g = 0
a = 0

for indi in reversed(range(0, len(pali))):
    if pali[indi] == pali[a]:
        g += 1 
    a += 1
if len(pali) == g:
    print('Es un palindromo')
else:
    print('NO es palindromo')