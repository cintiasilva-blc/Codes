'''Faça um algoritmo para ler 5 números DIFERENTES a serem armazenados em uma lista. Caso o usuário
digite um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número.
Note que cada valor digitado pelo usuário deve ser pesquisado na lista, verificando se ele existe entre os
números que já foram fornecidos. Exibir na tela a lista final que foi formada.'''

lista = []

for n in range(5):
    num = int(input("Digite um número inteiro ",n+1,'(diferente dos outros)')) 
    if n in num:
        print('Digite outro número: ')
        num = int(input("Digite um número inteiro ",n+1,'(diferente dos outros)'))
    lista.append(num)
    print('A lista formada é: ', lista)