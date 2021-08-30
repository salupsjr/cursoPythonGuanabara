alt = float(input('Qual a altura da parede? (em metros) '))
larg = float(input('Qual a largura da parede? (em metros) '))

area = larg * alt

qntTinta = area/2

print('A área total da sua parede é de {}m² e a quantidade de tinta necessária é de {:=.1f} litros.'.format(area, qntTinta))