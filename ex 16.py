# 16 Matriz de Soma Máxima -  Dada uma matriz 2D de números, encontre o subconjunto de tamanho k x k que tem da máxima soma.

def matriz_soma_maxima(matriz, k):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    # Verificando se o subconjunto kxk cabe na matriz original
    if k > linhas or k > colunas:
        print("O valor de k é muito grande para a matriz fornecida.")
        return None

    max_soma = float('-inf')  # Inicializando com o menor valor possível
    melhor_submatriz = []

    # Percorrer todas as possíveis submatrizes kxk
    for i in range(linhas - k + 1):
        for j in range(colunas - k + 1):
            soma_atual = 0
            # Somar os elementos da submatriz kxk
            for x in range(i, i + k):
                for y in range(j, j + k):
                    soma_atual += matriz[x][y]

            # Se a soma atual for maior que a soma máxima, atualize
            if soma_atual > max_soma:
                max_soma = soma_atual
                melhor_submatriz = [linha[j:j+k] for linha in matriz[i:i+k]]

    return max_soma, melhor_submatriz


# Função para ler a matriz do usuário
def ler_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        print(f"Digite os elementos da linha {i+1}:")
        for j in range(colunas):
            valor = int(input(f"Elemento [{i+1},{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

# Função para imprimir a matriz
def imprime_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

# Programa principal
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = ler_matriz(linhas, colunas)

print("Matriz fornecida:")
imprime_matriz(matriz)

k = int(input("Digite o tamanho k da submatriz (kxk): "))

# Encontrar a submatriz kxk com a soma máxima
resultado = matriz_soma_maxima(matriz, k)

if resultado:
    max_soma, submatriz = resultado
    print(f"\nSubmatriz {k}x{k} com a maior soma ({max_soma}):")
    imprime_matriz(submatriz)
