'''nome = str(input('Qual é o seu nome? '))

#CONDIÇÃO SIMPLES 
if nome == 'Junior':
   print('Que lindo nome você tem!!!')

print('Bom dia, {}!!!'.format(nome))'''

'''#CONDIÇÃO COMPOSTA
if nome == 'Junior':
   print('Que lindo nome você tem!!!')
else: 
   print('Que nome normal...rs')

print('Bom dia, {}!!!'.format(nome))'''

#CONDIÇÃO SIMPLIFICADA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

print('Sua média foi {:.1f}'.format(m))

print("Parabéns!!!" if m >= 6 else "Estude um pouco mais.")