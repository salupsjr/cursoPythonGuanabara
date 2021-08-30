nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiusculo é', nome.upper())
print('Seu nome em minusculo é', nome.lower())

#nomeSemEspaço = nome.replace(' ', '') #Minha solução 
#print('Seu nome tem {} letras.'.format(len(nomeSemEspaço))) #Minha solução

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))


#encontraEspaco = nome.find(' ')#Minha solução
#print('Seu primeiro nome é {}, certo?'.format(nome[:encontraEspaco]))#Minha solução   

#print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))) #Solução 1 guanabara

separa = nome.split()
print('Seu primeiro é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))