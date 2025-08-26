'''Peça uma palavra ao usuário (input) e guarde essa
palavra em uma variável. Imprima no terminal apenas os
caracteres dessa palavra que não são vogais utilizando
For.'''

var = str(input('Digite uma palavra: '))

for i in var :
    if i != 'a' and i != 'o' and i != 'e' and i != 'i' and i != 'u':
        print(i)