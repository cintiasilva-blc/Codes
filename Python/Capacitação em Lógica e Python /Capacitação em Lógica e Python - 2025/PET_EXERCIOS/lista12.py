'''Um aluno está cursando três disciplinas e precisa ser aprovado em todas elas para passar de ano. Para ser
aprovado, a média em cada disciplina deve ser maior que 7.'''

Media1 = int(input('Média 1: '))
Media2 = int(input('Média 2: '))
Media3 = int(input('Média 3: '))

if Media1 > 7 and Media2 > 7 and Media3 > 7 :
    print('Parabéns!! Você foi aprovado.')
else:
    print(':(( Você foi Reprovado! Boa sorte no próximo ano!')