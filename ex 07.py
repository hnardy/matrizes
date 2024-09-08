#Uma matriz triangular superior é aquela em que todos os elementos abaixo da diagonal principal são zero.
#De forma semelhante, uma matriz triangular inferior é aquela em que todos os elementos acima da diagonal principal são zero.
#Como você pode identificar se uma matriz é triangular superior ou inferior, em C e Python:
#em pyrhon



def diag_superior(m):
    #considerando sempre uma matriz quadrada
    colunas = len(m)
    linhas = len(m[0])
    diagSup = 0

    for i in range(colunas):
        for j in range(linhas):
            if i < j:
                diagSup += m[i][j]
    if diagSup == 0:
        print("matriz triangular inferior")
    else:
        print("matriz não triangular inferior")


def diag_inferior(m):
    #considerando sempre uma matriz quadrada
    colunas = len(m)
    linhas = len(m[0])
    diagInf = 0

    for i in range(colunas):
        for j in range(linhas):
            if i >  j:
                diagInf += m[i][j]
    if diagInf == 0:
        print("matriz triangular superior")
    else:
        print("matriz não triangular superior")


matriz = [[1, 0, 0],
          [0, 5, 0],
          [1, 0, 9]]
diag_superior(matriz)
diag_inferior(matriz)