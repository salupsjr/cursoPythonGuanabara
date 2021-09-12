
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
        
print('Você digitou {} números PARES e a soma deles é de {}.'.format(cont, soma))