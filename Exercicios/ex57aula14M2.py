sexo = str(input('Digite seu sexo [M / F]: ')).strip().upper()[0] #TIRA OS ESPAÇOS(.STRIP()), TRANFORMA EM MAIUSCULA(.UPPER()) E PEGA SÓ A PRIMEIRA LETRA ([0])
nSexo = ''
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite seu sexo [M / F]: ')).strip().upper()[0]


if sexo == 'M':
    nSexo = 'Masculino'
elif sexo == 'F':
    nSexo = 'Feminino'
            
print('Sexo {}-{} registrado com sucesso.'.format(sexo, nSexo)) 