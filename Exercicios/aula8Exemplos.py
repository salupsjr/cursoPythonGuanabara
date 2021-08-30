#-*-coding:utf8;-*-
#qpy:console

#EXEMPLOS DE IMPORTAÇÃO DE BIBLIOTECAS PYTHON

#import math #Importação da biblioteca matemática math completa. 

from math import sqrt, floor #Importação da biblioteca math somente com as funções de raiz quadrada (sqrt) e arredondamento para baixo(floor)

num = int(input('Digite um número: '))

raiz = sqrt(num) # Se for importado somente a biblioteca se coloca math.sqrt(...)

print('A raiz de {} é {}.'.format(num, floor(raiz)))