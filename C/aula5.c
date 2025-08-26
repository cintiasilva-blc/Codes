//VARIÁVEIS
// char: string                     char[(num. max de caracteres)]
// int: número inteiro
// float: número real

// #define: atribui um valor constante
// nomenclatura de variáveis -> tipo nome = valor

#include <stdio.h>
#define texto "Entrada e saída de dados."

int main() {
    printf("%s\n", texto);

    int idade = 0;
    float altura = 0.0;
    char nome[50] = "";

    printf("Digite sua idade:\n");
    scanf("%d", &idade);

    printf("Digite sua altura:\n");
    scanf("%f", &altura);

    printf("Digite o nome:\n");
    scanf("%s", nome);

    printf("dados informados:\n");
    printf("Idade: %d.\n", idade);
    printf("Altura: %2f.\n", altura);
    printf("Nome: %s.\n", nome);

}