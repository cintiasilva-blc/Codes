//ESPECIFICADORES DE FORMATO (scanf)
// todos os anteriores
//  [^chars] : lê todos od dados digitados, exceto os especificados em "chars"

#include <stdio.h>

int main(){

    int idade = 0;
    int ano = 1950;

    printf("Digite uma idade:\n");
    printf("Digite um ano:\n");
    scanf("%d %d", &idade, &ano);

    printf("Idade informada: %d.\n", idade);
    printf("Ano Informado: %d.\n", ano);
}