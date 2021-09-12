soma = 0
quant = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c 
        quant += 1 
print('A soma de todos os {} valores solicitados é de {}.'.format(quant, soma))