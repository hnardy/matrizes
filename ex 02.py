# ex 02
#Leia uma matriz 3x3 e imprima sua diagonal principal.


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



def imprime_diag_principal(m):
    #considerando que a matriz será sempre quadrada

    tam = len(m)
    principal = list()
    for i in range(tam):
        for j in range(tam):
            if i == j:
                principal.append(m[i][j])
    print(f'matriz principal:{principal}')


mat = gerar_matriz_aleatoria()
imprime_matriz(mat)
imprime_diag_principal(mat)
