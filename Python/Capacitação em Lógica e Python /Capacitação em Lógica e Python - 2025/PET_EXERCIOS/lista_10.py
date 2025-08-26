'''Faça um algoritmo que leia um valor em minutos e permita convertê-lo para horas, segundos e dias.
> 1 hora = 60 minutos
> 1 minuto = 60 segundos
> 1 dia = 1440 minutos
'''

min = int(input('Minutos: '))

hrs = min / 60
segundos = min * 60
dias = min / 1440

print('O resultado das conversções é: ')
print('Segundos: ',round(segundos))
print('Horas: ',round(hrs,2))
print('Dias: ',round(dias))
