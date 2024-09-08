#include <stdio.h>
#include <limits.h> // Para usar INT_MIN

#define MAX 100

// 15. Matriz de Soma Máxima Dada uma matriz 2D de números, encontre o subconjunto de tamanho k x k que tem a máxima soma. com solução em C em python


int calcular_soma(int matriz[MAX][MAX], int x, int y, int k) {
    int soma = 0;
    for (int i = x; i < x + k; i++) {
        for (int j = y; j < y + k; j++) {
            soma += matriz[i][j];
        }
    }
    return soma;
}

// Função para encontrar o subconjunto kxk com a maior soma
void matriz_soma_maxima(int matriz[MAX][MAX], int linhas, int colunas, int k) {
    int max_soma = INT_MIN;  // Inicializando com o menor valor possível
    int melhor_x = 0, melhor_y = 0; // Posições da melhor submatriz

    // Percorrer todas as possíveis submatrizes kxk
    for (int i = 0; i <= linhas - k; i++) {
        for (int j = 0; j <= colunas - k; j++) {
            int soma_atual = calcular_soma(matriz, i, j, k);

            // Atualizar a maior soma encontrada
            if (soma_atual > max_soma) {
                max_soma = soma_atual;
                melhor_x = i;
                melhor_y = j;
            }
        }
    }

    // Imprimir a submatriz de soma máxima
    printf("Submatriz %dx%d com a maior soma (%d):\n", k, k, max_soma);
    for (int i = melhor_x; i < melhor_x + k; i++) {
        for (int j = melhor_y; j < melhor_y + k; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }
}

// Programa principal
int main() {
    int linhas, colunas, k;
    int matriz[MAX][MAX];

    printf("Digite o número de linhas da matriz: ");
    scanf("%d", &linhas);
    printf("Digite o número de colunas da matriz: ");
    scanf("%d", &colunas);

    // Ler a matriz
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            printf("Elemento [%d,%d]: ", i + 1, j + 1);
            scanf("%d", &matriz[i][j]);
        }
    }

    printf("Digite o tamanho k da submatriz (kxk): ");
    scanf("%d", &k);

    // Encontrar e imprimir a submatriz de soma máxima
    matriz_soma_maxima(matriz, linhas, colunas, k);

    return 0;
}
