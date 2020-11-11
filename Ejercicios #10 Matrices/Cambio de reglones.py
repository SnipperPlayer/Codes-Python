#Emmanuel Galeana
#04/10/2020
#Cambio de renglones

def cmatriz():
    r = 2
    c = 2
 
    matrix = [ [int(input()) for c in range(c)] for r in range(r)]
    return matrix
def cambio(mat):
    c1 = int(input())
    c2 = int(input())
    lista1 = mat[c1]
    lista2 = mat[c2]
    mat[c2] = lista1
    mat[c1] = lista2
    print(mat)

mat=(cmatriz())
cambio(mat)
