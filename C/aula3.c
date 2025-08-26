// ESPECIFICADORES DE FORMATO (printf)
// Num Inteiros em base decimal: d ou i
// Num inteiro em base hexadecimal: X
// Num em notação científica: e
// Caracteres alfanuméricos(texto): c , ex: 'a'
// Sequência de caracteres: s , ex: "abcde"
// <num> : específica quantos números serão impressos após a virgula

// SEQUÊNCIAS DE ESCAPE (printf)
// \a : toca um alarme padão do sistema
// \b : backspace
// \n : quebra de linha
// \t : TAB
// \O : caractere nulo
// \v : tabulação vertical
// \\ : '\'
// \' : '
// \" : ""
// \? : ?
// ASCII : '\(cod em ascii)'


//

#include <stdio.h>

int main(){

    printf("Oi, tudo bem? Tenho 6 anos e programo.\n");

    printf("Valor INTEIRO: %d.\n", 10);
    printf("Valor real: %f.\n", 3.14159265);
    printf("Valor real com apenas duas casas: %.2f.\n", 3.14159265);
    printf("Dado de texto: %c.\n", 'A');
    printf("Dado de texto: %s.\n", "testando");

}



















