#-*-coding:utf8;-*-
#qpy:console

z = input('Digite qualquer coisa: ')

print('O tipo primitivo do que você digitou é {}'.format(type(z)))

print('O que você digitou é número? Resp.:',z.isnumeric())
print('O que você digitou é letra? Resp.:',z.isalpha())