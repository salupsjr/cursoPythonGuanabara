valor =  float(input('Quantos reais você tem na carteira? '))

conv = valor / 5.2

print('Você pode comprar {:=.2f} Dolares com seus {:=.2f} Reais.'.format(conv, valor))