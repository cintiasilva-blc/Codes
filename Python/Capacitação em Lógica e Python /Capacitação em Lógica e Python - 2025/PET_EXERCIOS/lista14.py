'''Crie um algoritmo que funcione como uma calculadora simples para as quatro operações básicas. O programa
deve pedir ao usuário dois números e a operação desejada. O programa deve realizar o cálculo correspondente
e mostrar o resultado.
> +, −, *, /'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
operacao = str(input('Qual operação você deseja fazer? (+ , - , * , /) '))

if operacao == '+':
    soma = num1 + num2
    print('Soma: ',soma)
elif operacao == '-':
    sub = num1 - num2
    print('Subtração: ',sub)
elif operacao == '*':
    mult = num1 * num2
    print('Multiplicação: ',mult)
elif operacao == '/':
    div = num1 / num2
    print('Divisão: ',div)