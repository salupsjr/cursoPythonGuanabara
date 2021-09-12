'''print('-=' * 20)
print('ANALISADOR DE PESO')
print('-=' * 20)

maiorPeso = 0
menorPeso = 999
for c in range(1,6):
    peso = float(input('Digite o {}º peso: '.format(c)))
    
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print('O maior peso é: {}'.format(maiorPeso))
print('O menor peso é: {}'.format(menorPeso))

'''
print('-=' * 20)
print('ANALISADOR DE PESO')
print('-=' * 20)
maiorPeso = 0
menorPeso = 0
for c in range(1,6):
    peso = float(input('Digite o {}º peso: '.format(c)))
    if c == 1:
        maiorPeso = c
        menorPeso = c
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O maior peso é: {}'.format(maiorPeso))
print('O menor peso é: {}'.format(menorPeso))