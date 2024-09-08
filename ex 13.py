# 13 . Matriz Simétrica / Verifique se uma matriz é simétrica ou não. (Uma matriz quadrada é chamada de simétrica se a matriz e sua transposta são iguais.)


def verificar_simetria(matriz):
    tam = len(matriz)
    for i in range(tam):
        for j in range(i, tam):  # Percorrer apenas metade superior da matriz
            if matriz[i][j] != matriz[j][i]:
                return False  # Se houver qualquer desigualdade, não é simétrica
    return True

# Função para ler uma matriz do usuário
def ler_matriz(tamanho):
    matriz = []
    for i in range(tamanho):
        linha = []
        print(f"Digite os elementos da linha {i+1}:")
        for j in range(tamanho):
            valor = int(input(f"Elemento [{i+1},{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

# Função para imprimir a matriz
def imprime_matriz(matriz):
    tam = len(matriz)
    for i in range(tam):
        for j in range(tam):
            print(f"| {matriz[i][j]} |", end="")
        print("")
    print("")

# Programa principal
tamanho = int(input("Digite o tamanho da matriz quadrada: "))
matriz = ler_matriz(tamanho)

print("Matriz inserida:")
imprime_matriz(matriz)

# Verificando se a matriz é simétrica
if verificar_simetria(matriz):
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")
