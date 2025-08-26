'''Escreva um algoritmo que peça ao usuário um número inteiro positivo. O programa deve então contar de 1 até
esse número, exibindo cada número na tela, um por vez. Use uma estrutura de repetição for realizar essa
contagem.'''

num = int(input('Digite um número inteiro: '))

for i in range(1, (num+1)):
    print(i)