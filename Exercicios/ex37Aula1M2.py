num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO.
[2] converter para OCTAL.
[3] converter para HEXADECIMAL.''')
opção = int(input('Sua opção: '))

if opção == 1:
      print('{} convertido para Binário é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
      print('{} convertido para Octal é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
      print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
      print('Opção inválida escolha entre opção 1, 2 ou 3')