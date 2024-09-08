#Função que verifica se a matriz é anti-simétrica

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

def verifica_simetria(matriz):
    tam = len(matriz)  

    simetrica=True
    antisimetrica=True

    for i in range(tam):
        for j in range(tam):
            if matriz[i][j] != matriz[j][i]:
                simetrica = False
            if matriz[i][j] != -matriz[j][i]:
                antisimetrica = False

    if simetrica and antisimetrica:
          return "A matriz é antissimetrica ou simetrica se for nula" 
    elif simetrica:
         return "A matriz é simétrica"
    elif antisimetrica:
         return "A matriz é antissimétrica"
    else: 
          return "A matriz não é nem simétrica e nem antissimétrica"

matriz = gerar_matriz_aleatoria()

print("a matriz gerada foi: ")
imprime_matriz(matriz)

resultado = verifica_simetria(matriz)
print(resultado)