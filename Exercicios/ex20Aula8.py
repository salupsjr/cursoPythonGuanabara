#-*-coding:utf8;-*-
#qpy:console

'''import random

a1 = str(input ('Nome do 1o aluno: '))
a2 = str(input('Nome do 2o aluno: '))
a3 = str(input ('Nome do 3o aluno: '))
a4 = str(input('Nome do 4o aluno: '))

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print(lista)'''

from random import shuffle

a1 = input('Nome aluno 1: ')
a2 = input('Nome aluno 2: ')
a3 = input('Nome aluno 3: ')
a4 = input('Nome aluno 4: ')

lista = [a1, a2, a3, a4]

shuffle(lista)

print(lista)