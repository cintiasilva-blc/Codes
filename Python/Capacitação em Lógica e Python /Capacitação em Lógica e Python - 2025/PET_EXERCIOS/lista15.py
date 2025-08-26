'''Faça um algoritmo que leia um número inteiro n informado pelo usuário e imprima sua tabuada de 1 até 10.'''

print('____TABUADA____')
num = int(input('Digite um número inteiro: '))

for i in range(1,11):
    tab = num * i
    print('Tabuada',num,'x',i,':',tab)
