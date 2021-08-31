from datetime import date
ano = int(input('Qual ano você deseja saber se é BISSEXTO ou não? R: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('Oano de {} NÃO É BISSEXTO.'.format(ano))