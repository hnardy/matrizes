#15. Rotacionar Matriz 90 Graus
#- Escreva um programa para rotacionar uma matriz em 90 graus no sentido horário.

# 1 passo transpor a matriz
# 2 passo trocar as colunas de ordem



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


def mudar_ordem(m):
    tam = len(m)
    m_aux = [[0 for i in range(tam)] for i in range(tam)]

    #clonar matriz para auxiliar
    for i in range(tam):
        for j in range(tam):
            m_aux[i][j] =m[i][j] # faz a inversão

    #inverter
    for i in range(tam):
        for j in range(tam):
            m[i][j] = m_aux[i][tam-j-1]

    return m

print("orientação original")
matriz = gerar_matriz_aleatoria()
imprime_matriz(matriz)
print()

matriz=inverter_matriz(matriz) #transpoe
#imprime_matriz(matriz)
print()

print("rotacionado 90°")
matriz = mudar_ordem(matriz) #muda as colunas
imprime_matriz(matriz)
