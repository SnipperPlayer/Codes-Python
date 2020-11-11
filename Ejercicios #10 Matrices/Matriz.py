#Emmanuel Galeana
#01/10/2020
"""
matriz = [['a', "''",'i'],
          ["''", 'e',"''"],
          ['a', "''",'i']]

    print(matriz[2][-2])

def matriz (columna, renglon):
    matriz1= [[input() for r in range(renglon)]for c in range(columna)]
    print(matriz1)

    matriz(int(input()), int(input()))
"""
def fun():
    mat = [['5', "4",'4'],
           ["4", '3',"4"],
           ['1', "4",'2']]
    new_mat =[]
    for ndx, row in enumerate(mat):
        if ndx==len(row)-1:
            new_mat.append(row)
        else:
            new_mat.append(([row[0]]) + (len(row)-1)*[''])
    print(new_mat)
fun()