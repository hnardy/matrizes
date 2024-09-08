#5. Adição de Matrizes
 # - Escreva um programa para adicionar duas matrizes.

from random import randint

def gerar_matriz_aleatoria(tam):
  #  tam = int(input("digite o tamanho da matriz quadrada")) #tamanho da matriz
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


def soma_matrizes(m1,m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0])   :
        print("ok")

        colunas =len(m1)
        linhas  =len(m1[0])

        for i in range(colunas):
            for j in range(colunas):
                m1[i][j] = m1[i][j] + m2[i][j]
        return m1









    else:
        print("as matrizes devem ser de tamanho igual!")





tam = int(input("digite o  tamanho da matriz"))
print("matriz 1")
matriz1 = gerar_matriz_aleatoria(tam)
imprime_matriz(matriz1)
print()
print("matriz 2")
matriz2 = gerar_matriz_aleatoria(tam)
imprime_matriz(matriz2)
print()
print("matriz resultado")
matriz_resultado = soma_matrizes(matriz1,matriz2)
imprime_matriz(matriz_resultado)
