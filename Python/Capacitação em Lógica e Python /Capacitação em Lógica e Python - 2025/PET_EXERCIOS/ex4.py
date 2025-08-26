''''Crie uma lista de números inteiros e gere uma nova
lista contendo apenas os números positivos (remova os
negativos). Imprima a lista após o processo.'''

lista_int = [1,-1,2,-2,3,-3]
lista_nat = []

for i in lista_int:
    if i >= 0:
        lista_nat.append(i)
        print(i)