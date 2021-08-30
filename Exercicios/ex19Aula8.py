#-*-coding:utf8;-*-
#qpy:console
'''import random

a1 = str(input('Informe o nome do primeiro aluno(a): '))
a2 = str(input('Informe o nome do segundo aluno(a): '))
a3 = str(input('Informe o nome do terceiro aluno(a): '))
a4 = str(input('Informe o nome do quarto aluno(a): '))

lista = [a1, a2, a3, a4]

escolhido = random.choice(lista)

print('O escolhido(a) foi {}.'.format(escolhido))'''

from random import choice

a1 = str(input('Informe o nome do 1° aluno: '))
a2 = str(input('Informe o nome do 2° aluno: '))
a3 = str(input('Informe o nome do 3° aluno: '))
a4 = str(input('Informe o nome do 4° aluno: '))

lista = [a1, a2, a3, a4]

escolhido = choice(lista)

print('O escolhido foi o aluno {}.'.format(escolhido))