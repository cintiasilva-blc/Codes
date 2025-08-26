senha = str(input('Crie uma senha: '))

continuar = True
while continuar:

    qual_senha = str(input('Qual é a senha? '))

    if senha == qual_senha:
        print('Senha Correta!;)\n')
        continuar = False
    else:
        print('A senha está incorreta! Tente Novamente ;(\n')
        continuar = True