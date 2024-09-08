#Função para ler uma matriz aleatória e escrevê-la respeitando a ordem espiral
#Matriz em espiral

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

def matriz_espiral(matriz):
    tam_linhas = len(matriz)
    tam_colunas = len(matriz[0])
    
    topo, baixo = 0, tam_linhas - 1
    esquerda, direita = 0, tam_colunas - 1
    
    print("Matriz em formato espiral:")
    while topo <= baixo and esquerda <= direita:
        
        for j in range(esquerda, direita + 1):
            print(matriz[topo][j], end=" ")
        topo += 1
        
        
        for i in range(topo, baixo + 1):
            print(matriz[i][direita], end=" ")
        direita -= 1
        
        
        if topo <= baixo:
            for j in range(direita, esquerda - 1, -1):
                print(matriz[baixo][j], end=" ")
            baixo -= 1
        
        if esquerda <= direita:
            for i in range(baixo, topo - 1, -1):
                print(matriz[i][esquerda], end=" ")
            esquerda += 1
    
    print()  
    


matriz = gerar_matriz_aleatoria()
print("A matriz é: ")
imprime_matriz(matriz)
matriz_espiral(matriz)      
