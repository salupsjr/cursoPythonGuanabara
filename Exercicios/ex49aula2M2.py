num = int(input('Digite o número para a tabuada: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num*c))