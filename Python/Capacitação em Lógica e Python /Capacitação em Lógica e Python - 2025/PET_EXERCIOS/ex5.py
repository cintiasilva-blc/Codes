'''Leia uma lista de números inteiros e um número
inteiro separado pelo usuário, e informe se esse número
está presente na lista ou não.'''

num_user = int(input('digite um número inteiro: '))
lista = [4,8,12,16]

for i in lista:
    if i == num_user:
       print(True)
print(False)
