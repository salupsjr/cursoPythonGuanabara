somaIdade = 0
mIdade = 0
nmVelho = ''
totMF = 0
p = int(input('Quantas pessoas deseja cadastrar? R: '))
for c in range(1, p+1):
    print('DADOS DA {}ª PESSOA'.format(c))
    nome = str(input('Digite o nome:')).strip()
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo [M / F]:')).strip().upper()
    somaIdade += idade
    if sexo in 'Mm' and idade > mIdade:
        mIdade = idade
        nmVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMF += 1
        
        
media = somaIdade / c    
print('A média de idade entre as {} pessoas é de {:.2f} anos.'.format(c, media))
print('O nome do homem mais velho é {} e a sua idade é {} anos.'.format(nmVelho, mIdade))
print('A quantidade de mulheres com menos de 20 anos é igual a {}.'.format(totMF))
