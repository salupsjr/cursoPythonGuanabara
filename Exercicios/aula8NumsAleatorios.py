#-*-coding:utf8;-*-
#qpy:console

#QUERO CRIAR UM PROJETO QUE ESCOLHA NÚMEROS
#ALEATORIOS PARA LOTERIAS ONDE O USUÁRIO ESCOLHE
#UM NÚMERO PARA O INÍCIO DOS NÚMEROS QUE ELE QUER CONTAR
#E ESCOLHE TAMBÉM ATE ONDE VAI ESSA CONTAGEM
#VERSÃO 1.0.0

import random

inicio = int(input('Informe o início da contagem:'))

fim = int(input('Informe o fim da contagem: '))


num = random.randint(inicio, fim)

print(num)
