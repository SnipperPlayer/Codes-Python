#Emmanuel Galeana
#21/09/2020
#Locura de letras

import unicodedata

def stri(a):
    text = unicodedata.normalize('NFD', a)\
            .encode('ascii', 'ignore')\
            .decode('utf-8')
    return str(text)

a = stri(input())

a = "".join(["3" if _.lower() == "e" else _ for _ in a])
a = "".join(["h" if _.lower() == "o" else _ for _ in a])
a = "".join(["4" if _.lower() == "a" else _ for _ in a])


print(a)