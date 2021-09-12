from datetime import date

print('-=' * 20)
print('ANALISADOR DE MAIORIDADE')
print('-=' * 20)
jovem = 0
adulto = 0
anoAtual = date.today().year
for c in range(1, 8):
    ano = int(input('Digite o {}º ano de nascimento:'.format(c)))
    idade = anoAtual - ano
    if idade <= 17:
        jovem += 1
    else:
        adulto += 1
print('O menores de idade são: {}.'.format(jovem))
print('Os maiores de idade são: {}'.format(adulto))