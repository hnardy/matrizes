#ex 3
# Transponha uma matriz 3x3 (troque linhas por colunas).

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

def inverter_matriz(m):
    tam = len(m)
    m_aux = [[0 for i in range(tam)] for i in range(tam)]

    #clonar matriz para auxiliar
    for i in range(tam):
        for j in range(tam):
            m_aux[i][j] =m[i][j] # faz a inversão

    #inverter
    for i in range(tam):
        for j in range(tam):
            m[i][j] = m_aux[j][i]

    return m


mat = gerar_matriz_aleatoria()
imprime_matriz(mat)
inv = inverter_matriz(mat)
print("="*30)
print("matriz invertida")
imprime_matriz(inv)