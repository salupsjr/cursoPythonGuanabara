dist = float(input('Qual é a distância da sua viagem? (em Km) R: '))
print('Você está prestes a começar uma viagem de {}km'.format(dist))
if dist <= 200:
    vpassagem = dist * 0.50
else: 
    vpassgem = dist * 0.45
    
print('O valor da sua passagem é de R${:.2f}.'.format(vpassagem))