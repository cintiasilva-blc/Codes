'''Criar um algoritmo que leia três números inteiros digitados pelo usuário e determine qual deles é o maior.'''

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
num3 = int(input('Digite um número inteiro: '))
print()
if num1 > num2 and num1 > num3:
    print('O maior número é: ', num1)
elif num2 > num1 and num2 > num3:
    print('O maior número é: ', num2)
else:
    print('O maior número é: ', num3)

print()