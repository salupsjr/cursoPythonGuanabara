#-*-coding:utf8;-*-
#qpy:console

nome = str(input ('Digite seu nome completo: ')).strip()

print(nome.split())

print('Seu primeiro nome é {}'.format(nome.split()[0]))

print('Seu último nome é {}'.format(nome.split()[-1]))
