#-*-coding:utf8;-*-
#qpy:console

'''
ENUNCIADO DO EXERCÍCIO 17
Faça um programa que leia o 
cateto oposto e o cateto adjacente de 
um triângulo retângulo.
Calcule e mostre o comprimento da 
hipotenusa.'''

#import math
from math import hypot
co = float(input('Qual é o comprimento do cateto oposto: '))
ca = float(input('Qual é o comprimento do cateto adjacente: '))

#hi = (co ** 2 + ca ** 2) ** (1/2) #Esse é usado sem precisar importar classes

#hi = math.hypot(co, ca) #Esse é usado importando toda a classe math

hi = hypot(co, ca) #Esse é usado importando a função hypot da classe math

print('O comprimento da hipotenusa é {:.2f}'.format(hi))

