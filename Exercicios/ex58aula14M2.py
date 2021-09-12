#-*-coding:utf8;-*-
#qpy:console
#MINHA SOLUÇÃO
from random import randint
print('Olá, sou o seu computador e...', end='')
num = int(input('''estou pensando em um número entre 0 e 10.
Você consegue advinhar? 
Qual o seu palpite? '''))
escolhido = randint(0, 10)
tentativas = 0
while escolhido != num:
    if escolhido > num:
        dica = 'Mais...'
    elif escolhido < num:
        dica = 'Menos...'        
    num = int(input('''{} Tente mais uma vez. 
Qual o seu palpite? '''.format(dica)))
    tentativas += 1
if num == escolhido:
    print('PARABÉNS, VOCÊ ACERTOU COM {} TENTATIVAS.'.format(tentativas))

'''#SOLUÇÃO GUANABARA
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Quak é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas.'.format(palpites))'''