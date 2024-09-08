#ex 11. Matriz Esparsa
# #Verifique se uma matriz é esparsa ou não. (Uma matriz é considerada esparsa se a maioria de seus elementos for zero.)


def contar_zeros(m):
    #considerando que a matriz sempre será quadrada
    colunas = len(m)
    linhas = len(m[0])
    zeros,nao_zeros= 0 , 0
    for i in range(linhas):
        for j in range(colunas):
            if m[i][j] == 0:
                zeros +=1
            else:
                nao_zeros+=1
    if zeros > nao_zeros:
        print("matriz esparsa")
    else:
        print("matriz não esparsa")


matriz_esparsa = [[0,1,0],[1,0,0],[0,0,1]]
contar_zeros(matriz_esparsa)

print()

matriz = [[1,2,3],[4,5,6],[7,8,9]]
contar_zeros(matriz)
