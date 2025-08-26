'''Crie um algoritmo que peça uma senha e verifique se ela atende a estes requisitos:
> Ter pelo menos 8 caracteres;
> Conter pelo menos uma letra maiúscula;'''
print()
print('____Requisitos para a Senha____')
print('> Ter pelo menos 8 caracteres;')
print('> Conter pelo menos uma letra maiúscula;')
senha = str(input('Digite uma senha: '))

comp_min = len(senha)
tem_maiuscula = False

for i in senha:
    if i.isupper():
        tem_maiuscula = True
        break

if comp_min and tem_maiuscula:
    print('Senha válida!')
else:
    if comp_min < 8:
        print('A senha prescisa ter pelo menos 8 caracteres!')
    if not tem_maiuscula:
        print('A senha prescisa ter pelo menos uma letra maiúscula!')



