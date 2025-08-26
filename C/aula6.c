//OPERADORES ARITMÉTICOS
// Soma: + , Subtração: - , Multiplicação: * , Divisão: / , Resto da Div: % .

#include <stdio.h>

int main() {
    int A, B, soma, sub, mult, div;

    printf("Digite um valor:\n");
    scanf("%d", &A);
    printf("Digite outro valor:\n");
    scanf("%d", &B);

    soma = A + B;
    sub = A - B;
    mult = A * B;
    div = A / B;

    printf("Resultados:\n");
    printf("Soma: %d.\n", soma);
    printf("Subtração: %d.\n", sub);
    printf("Multiplicação: %d.\n", mult);
    printf("Divisão: %d.\n", div);

}

//OPERADORES DE ATRIBUIÇÃO ARITMETICA
// Incremento de 1 uni.: ++
// Decremento de 1 uni.: --
// Incremento Genérico: +=
// Decremento Genérico: -=
// Atribuição com multiplicação: *=
// Atrib. com Divisão: /=


