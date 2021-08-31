#-*-coding:utf8;-*-
#qpy:console

from random import randint
from time import sleep
print('-=-=-' * 10)
print('Estou pensando em um número...')
print('-=-=-' * 10)
num = int(input('Qual foi o número que pensei? R: '))


escolhido = randint(0, 5)
print('\nPROCESSANDO...\n')
sleep(3)
if num == escolhido:
    print('PARABÉNS, VOCÊ VENCEU!!! O NÚMERO {} ESTÁ CORRETO.'.format(num))
else:
    print('QUE PENA, PERDEU!!! O NÚMERO ESCOLHIDO FOI {} E VOCÊ ESCOLHEU {}, TENTE NOVAMENTE.'.format(escolhido, num))