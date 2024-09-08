#ex01
#Leia uma matriz 3x3 e calcule a soma de todos os seus elementos.

from random import randint


def gerar_matriz_aleatoria():
    tam = int(input("digite o tamanho da matriz quadrada")) #tamanho da matriz
    m = [[0 for j in range(tam)] for i in range(tam)] #matriz gerada com 0

    for i in range(0,tam):      #matriz preenchida com elemnentos aleatórios
        for j in range(0,tam):
            m[i][j] = randint(0,9)
            #print(m[i][j])
    return m


def imprime_matriz(m):
    #considerando que a matriz será sempre quadrada

    tam = len(m)
    for i in range(tam):
        for j in range(tam):
            print(f"| {m[i][j]} |", end="")
        print("")


def somar_matriz(m):
    # considerando que a matriz será sempre quadrada
    tam = len(m)
    soma = 0
    for i in range(tam):
        for j in range(tam):
            soma+= m[i][j]
    return soma



mat = gerar_matriz_aleatoria()
soma = somar_matriz(mat)
imprime_matriz(mat)
print(f"valor da soma {soma}")

