n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2 
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A Soma entre {} e {} é {}, a Multiplicação é {}, a Divisão é {:=.2f}'.format(n1, n2, s, m, d), end = ' ')
print('O resto da Divisão inteira é {} e a Potência é {}.'.format(di, e))