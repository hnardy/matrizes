#Função para multiplicar duas matrizes quadradas de tamanho igual

from random import randint


def gerar_matriz_aleatoria():
    tam = int(input("digite o tamanho da matriz quadrada")) 
    m = [[0 for j in range(tam)] for i in range(tam)] 

    for i in range(0,tam):    
        for j in range(0,tam):
            m[i][j] = randint(0,9)
            #print(m[i][j])
    return m


def imprime_matriz(m):
    
    tam = len(m)
    for i in range(tam):
        for j in range(tam):
            print(f"| {m[i][j]} |", end="")
        print("")

def multiplicar_matrizes(m1, m2):
    tam = len(m1)
    resultado = [[0 for _ in range(tam)] for _ in range(tam)]

    
    for i in range(tam):
        for j in range(tam):
            for k in range(tam):
                resultado[i][j] += m1[i][k] * m2[k][j]

    return resultado        

matriz1 = gerar_matriz_aleatoria()
matriz2 = gerar_matriz_aleatoria()

print("Matriz 1: ")
imprime_matriz(matriz1)
print("Matriz 2: ")
imprime_matriz(matriz2)

resultado = multiplicar_matrizes(matriz1,matriz2)

print("Matrizes multiplicadas: ")
imprime_matriz(resultado)
