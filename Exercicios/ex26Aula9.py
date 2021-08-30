frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "a" aprarece na frase {} vezes.'.format(frase.count('A')))

print('A letra "a" foi encontrada pela primeira vez na posição {}.'.format(frase.find('A')+1))

print('A letra "a" aparece pela ultima vez na posião {} da frase.'.format(frase.rfind('A', )+1))