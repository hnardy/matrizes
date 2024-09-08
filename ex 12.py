# Diagonal Principal e Secundária
# Calcule a soma dos elementos da diagonal principal e da diagonal secundária de uma matriz quadrada.

#
from random import randint


def gerar_matriz_aleatoria():
    tam = int(input("Digite o tamanho da matriz quadrada: "))  # tamanho da matriz
    m = [[0 for j in range(tam)] for i in range(tam)]  # matriz gerada com 0

    for i in range(0, tam):  # matriz preenchida com elementos aleatórios
        for j in range(0, tam):
            m[i][j] = randint(0, 9)
    return m


def imprime_matriz(m):
    # considerando que a matriz será sempre quadrada
    tam = len(m)
    for i in range(tam):
        for j in range(tam):
            print(f"| {m[i][j]} |", end="")
        print("")
    print("")  # separação entre impressões


def somar_matriz(m):
    # considerando que a matriz será sempre quadrada
    tam = len(m)
    soma = 0
    for i in range(tam):
        for j in range(tam):
            soma += m[i][j]
    return soma


def rotacionar_matriz_90_graus(m):
    """Função para rotacionar a matriz em 90 graus no sentido horário"""
    tam = len(m)
    # Cria uma matriz de mesma dimensão
    matriz_rotacionada = [[0 for _ in range(tam)] for _ in range(tam)]

    # Executa a rotação
    for i in range(tam):
        for j in range(tam):
            matriz_rotacionada[j][tam - 1 - i] = m[i][j]
    
    return matriz_rotacionada


# Gerar a matriz
mat = gerar_matriz_aleatoria()

# Imprimir a matriz original
print("Matriz original:")
imprime_matriz(mat)

# Somar elementos da matriz
soma = somar_matriz(mat)
print(f"Valor da soma: {soma}")

# Rotacionar a matriz em 90 graus
mat_rotacionada = rotacionar_matriz_90_graus(mat)

# Imprimir a matriz rotacionada
print("Matriz rotacionada 90 graus (sentido horário):")
imprime_matriz(mat_rotacionada)
