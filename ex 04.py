#4. Mini Projeto: Vamos criar uma aplicação simples para análise de vendas de produtos em uma loja durante determinados meses. A matriz armazenará o valor das vendas
#de produtos diferentes ao longo dos meses. A análise fornecerá:
#1. Vendas totais de cada produto durante todos os meses.
#2. Vendas totais de todos os produtos em um mês específico.
#3. Venda média mensal de cada produto.
#Vamos considerar 3 produtos e 12 meses.


#                   estrutura
#                 j=0  j=1 j=2 j=3 j=4 j=5 j=6 j=7 j=8 j=9 j10 j11
#                 jan  fez mar abr mai jun jul ago set out nov dez
#i = 0 produto 1
#i = 1 produto 2
#1 = 2 produto 3

from random import randint


def gerar_tabela(quanti_produtos= 3, messes= 12):

    m = [[0 for j in range(quanti_produtos)] for i in range(messes)]

    for j in range(0,quanti_produtos):
        for i in range(0,12):
            m[i][j] = randint(0,10)

    return m


def imprimir_tabela(m):
    #considerando que a matriz sempre será retangular
    colunas = len(m)
    linhas =len(m[0])

    print("            jan   fev   mar   abr   mai   jun   jul   ago   set   out   nov   dez")
    for j in range(0,linhas):
        print(f'produto: {j+1}', end= "")
        for i in range(0,colunas):

            print( f" | {m[i][j]} |", end= "")
        print("")


def vendas_totais_por_produto(m):
    # considerando que a matriz sempre será retangular
    colunas = len(m)
    linhas = len(m[0])
    somador= 0

    print("vendas totais por produto")
    for j in range(0,linhas):
        print(f'produto: {j + 1}', end="")
        for i in range(0,colunas):
          somador += m[][]
        print(somador)
        somador = 0



matriz = gerar_tabela(3,12)
print("tabela ")
imprimir_tabela(matriz)
vendas_totais_por_produto(matriz)




