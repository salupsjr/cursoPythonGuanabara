#AULA SOBRE STRING/CADEIA DE CARACTERES.

#O NOME DESSE PROCESSO É DA AULA É FATIAMENTO.

frase = 'Curso em Video Python'

#print(frase[9])#RESULTADO ESPERADO DESSA FRASE É O RETORNO V

#print(frase[9:14])#INDICA O INDICE INICIAL E O INDICE FINAL DA LEITURA E RETORNA O PALAVRA VIDEO

#print(frase[9:21:2])#INDICA O INDICE INICIAL, O INDICE FINAL  E QUANTOS INDICES ELE IRA PULAR PARA MOSTRAR AS LETRAS NA TELA.

#print(frase[:5])#O FATIAMENTO VAI DA 1A LETRA ATÉ A 5A MOSTRANDO A PALAVRA CURSO.ArithmeticError

#print(frase[15:])#O FATIAMENTO VAI DO INDICE 15 ATÉ O ÚLTIMO INDICE.

#print(frase[9::3])#INDICA O INDICE 9 COMO INICIAL E VAI ATE O FIM DA FRASE PULANDO DE 3 EM 3.

#ANALISE DE STRING

#print(len(frase)) #MOSTRA O TAMANHO/QUANTIDADE DE STRING #MUITO IMPRTANTE E USADO EM PROGRAMAÇÃO

#print(frase.count('o'))#Conta quantas letras "o" são encontradas.
#print(frase.count('o',0,13))#Conta quantas letras "o" são encontradas do inicio da frase ate o indice 13

#print(frase.find('Video'))#Procura na frase o indice em que se inicia a palavra "Video"

#print(frase.find('Android'))#Como a palavra não existe na frase será retornado -1(false), ou seja, não encontrado.

#print('Video' in frase)#Verifica se existe a palavra indicada dentro da variável/frase

#TRANFORMAÇÃO DE STRING
'''fraseNova = frase.replace('Python', 'Android')
print(fraseNova)#Tranforma a palavra indicada para a nova palavra.'''

'''print(frase.upper())#Mostra a frase toda em maiuscula
print(frase.lower())#Mostra a frase toda em minusculo
print(frase.capitalize())#Mostra a frase com a 1a letra maiuscula e o restante minuscula
print(frase.title())#Mostra a primeira letra de cada palavra da frase em maiuscula'''

#frase2 = '   Aprenda Python  '

'''frase2Nova = frase2.strip()

print(frase2Nova)#Exclui todos os espaços antes e depois da frase'''

'''frase2nova = frase2.rstrip()

print(frase2nova)#Exclui todos os espaços a direita da frase

frase2nova = frase2.lstrip()

print(frase2nova)#Exclui todos os espaços a esquerda da frase'''

#DIVISÃO DE STRING

print(frase.split())
print('-'.join(frase))

