print('___CAIXA ELETRÔNICO___')

saldo = int(input('Digite seu saldo atual: R$'))
opcao = 0

while opcao != 4 :
    opcao = int(input('O que você deseja fazer:\nSacar: [1]\nDepositar: [2]\nVer o seu saldo: [3]\nSair: [4].\n'))

    if opcao == 1:
        saque = int(input('Quanto você deseja sacar? R$'))
        saldo = saldo - saque
        print('Seu saldo restante é: R$ ', saldo)
        if saque >= saldo:
           saldo = 0
           print('Você não tem esse valor disponivel para saque. ;(')

    elif opcao == 2:
        deposito = int(input('Quanto você deseja depositar? R$'))
        saldo = saldo + deposito
        print('Seu saldo restante é: R$',saldo)

    elif opcao == 3:
        print('Seu saldo atual é: R$', saldo)

if opcao == 4:
   print('Fim.')




#########CORRIGIR#########
