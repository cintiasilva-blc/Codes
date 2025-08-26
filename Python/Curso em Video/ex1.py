print('SOMA DOIS NÚMEROS')
num1 = float(input('Digite um número inteiro:' ))
num2 = float(input('Digite um número inteiro:' ))

soma = num1 + num2
print('A soma entre {} e {} vale: {}'.format(num1, num2, soma))
print()


print('DISSECANDO UMA VARIÁVEL')
algo = input('Digite algo: ')
print('O tipo primitivo dessa variavel é: ',type(algo))
print('Só tem espaços? ', algo.isspace())
# varialvel.isspace(): verifica se a variável possui somente espaços
print('É um número? ', algo.isnumeric())
# varialvel.isnumeric(): verifica se a variável é um numero
print('é alfabetico? ', algo.isalpha())
# varialvel.isalpha(): verifica se a variável possui somente letras
print('é alfanumerico? ', algo.isalnum())
# varialvel.isalnum(): verifica se a variável possui letras e números
print('Estao em maiusculas? ', algo.isupper())
# varialvel.isupper(): verifica se a variável esta somente em letras maiusculas
print('Estao em minusculas? ', algo.islower())
# varialvel.islower(): verifica se a variável esta somente em letras minusculas
print('Esta capitalizada?', algo.istitle())
# varialvel.istitle(): verifica se a variável esta capitalizada
print()


div = num1 / num2
print('A divião é: {:.2f}'.format(div))
print()

print('ANTECESSOR E SUCESSOR')
print('O antecessor de {} é: {}\nO sucessor de {} é: {}'.format(num1, (num1 - 1), num1, (num1 + 1)))
print()

print('DOBRO, TRIPLO, RAIZ QUADRADA')
print('O dobro de {} é: {}'.format(num1, (num1 * 2)))
print('O triplo de {} é: {}'.format(num1, (num1 * 3)))
print('A raiz quadrada de {} é: {}'.format(num1, (num1 ** (1/2))))
print()

print('MEDIA ARITMETICA')
media = (num1 + num2) / 2
print('A média aritmética entre {:.1f} e {:.1f} é: {:.1f}'.format(num1, num2, media))
print()

print('CONVERSOR DE MEDIDAS')
cm = num1 * 100
ml = num1 * 1000
print('{} metros equivale a: {} centímetros'.format(num1, cm))
print('{} metros equivale a: {} milimetros'.format(num1, ml))
print(
    
)





