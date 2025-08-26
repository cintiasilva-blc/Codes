#ex2
'''Crie uma lista com cinco nomes, então imprima no
terminal apenas os nomes com mais de seis letras
utilizando For'''

lista = ['Cintia', 'Giovana', 'Ana', 'Nikolas', 'Kauã']

for i in lista:
    if len(i) > 6 :
        print(i)