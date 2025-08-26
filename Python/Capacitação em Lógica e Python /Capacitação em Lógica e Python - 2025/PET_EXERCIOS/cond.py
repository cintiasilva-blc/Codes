print('=====FAIXA ETARIA=====')
idade = int(input('Insira sua idade:'))

if idade <= 17:
    print('Menor de Idade')
elif (idade >= 18) and (idade < 60):
    print('Maior de Idade')
else:
    print('Idoso')



print('=====MEDIA NOTAS=====')
n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 + n3)/3

if media >= 6.0:
    print('Aprovado')
else:
    print('Exame')