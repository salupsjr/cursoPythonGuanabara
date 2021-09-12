n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
d = n + (10 - 1) * r

for c in range(n, d + r, r):
    print('{}'.format(c), end=' > ')
    
print('ACABOU!')

#ESSE EU BUGUEI. ESTUDAR PROGREÇÃO ARITMÉTICA.