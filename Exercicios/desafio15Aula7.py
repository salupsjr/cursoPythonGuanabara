#-*-coding:utf8;-*-
#qpy: console

#Escreva um programa qua pargunta a 
#quantidada da Km parcorridos por um 
#carro alugado e a quantidada de dias 
#pelos quais ele foi alugado. 
#Calcule o preço a pagar. 
#sabando que o carro custa RS60 por dia
# a RS0.15 por Km rodado.


qtdKm = float(input ('Quantos quilômetros foram percorridos? R:'))

qtdDia = float(input ('Foram quantos dias de aluguel do veículo? R:'))


custoDias = qtdDia * 60

custoKm = qtdKm * 0.15

custoTotal = custoDias + custoKm

print('O veículo foi alugado por {:.0f} dias e o valor total referente aos dias é de R${:.2f}.'.format(qtdDia, custoDias))

print('A quilometragem percorrida foi de {}Km e o custo total referente a quilometragem é de R${}'.format(qtdKm, custoKm))