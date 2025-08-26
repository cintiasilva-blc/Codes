continuar = True
while continuar:
    num1 = int(input('Digite um numero inteiro: '))
    num2 = int(input('Digite um numero inteiro: '))

    soma = num1 + num2 
    print(soma)
    x = int(input('Digite 1 para continuar: '))

    if x != 1:
        continuar = False