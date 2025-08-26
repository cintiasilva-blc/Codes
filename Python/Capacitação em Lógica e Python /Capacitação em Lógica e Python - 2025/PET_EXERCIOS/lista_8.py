'''Crie um algoritmo que solicite ao usuário dois números inteiros. Em seguida, o programa deve calcular a
soma, a subtração, a multiplicação e a divisão entre esses dois números e exibir os resultados de forma
organizada na tela, indicando qual é o resultado de cada operação. Se o segundo número for zero, informe que
a divisão não é possível.'''

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))

print('___SOMA___')
soma = num1 + num2
print(f'A soma entre {num1} e {num2} é igual a: {soma}')

print('___SUBTRAÇÃO___')
sub = num1 - num2
print(f'A diferença entre {num1} e {num2} é igual a: {sub}')

print('___MULTIPLICAÇÃO___')
mult = num1 * num2
print(f'O produto de {num1} e {num2} é igual a: {mult}')

print('___DIVISÃO___')
if num2 == 0:
    print('A divisão entre esses númreos não é possivel.')
else:
    div = num1 // num2
    print(f'A divisão entre {num1} e {num2} é igual a: {mult}')