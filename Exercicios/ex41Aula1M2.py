#-*-coding:utf8;-*-
#qpy:console

from datetime import date
print('CATEGORIZAÇÃO DE ATLETAS DO CLUBE')
print('TIPOS DE CATEGORIA: \n[MIRIM] DE 4 - 8 anos \n[INFANTIL] DE 9 - 14 anos \n[JUNIOR] DE 15 - 19 anos \n[SÊNIOR] DE 20 -25 anos \n[MASTER] DE ACIMA DE 26 anos')
ano = int(input ('Qual o ano de nascimento do atleta: '))
idade = date.today().year - ano

if idade <= 9:
    print('O atleta tem {} anos e se enquadra na categoria: MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e se enquadra na categoria: INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e se enquadra na categoria: JUNIOR.'.format(idade))
elif idade <= 25: 
    print('O atleta tem {} anos e se enquadra na categoria: SÊNIOR.'.format(idade))
elif idade >= 26:
    print('O atleta tem {} anos e se enquadra na categoria: MASTER.'.format(idade))