print('=-' * 20)
print('Analizador de Triângulos')
print('=-' * 20)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os SEGMENTOS acima PODEM formar um Triângulo.')  
else:
    print('Os SEGMENTOS acima NÂO PODEM formar um Triângulo.')