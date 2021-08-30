medida = float(input('Quantos metros você quer converter: '))

cent = (medida * 100)/1
mili = (medida * 1000)/1

print('{} metros convertidos para centrimetros é {}.'.format(medida, cent))
print('{} metros convertidos para milimetros é {}.'.format(medida, mili))