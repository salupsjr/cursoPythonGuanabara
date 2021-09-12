frase = str(input('Digite uma frase: ')).strip().upper() #RECEBE A FRASE, TIRA OS ESPAÇOS ANTES E DEPOIS DA MESMA E A COLOCA EM MAIUSCULA. 
p = frase.split() # QUEBRA A FRASE ENTRE OS ESPAÇOS E CRIA UMA LISTA
j = ''.join(p)# NESSE CASO TIRA TODOS OS ESPAÇOS DA FRASE COLANDO TODAS AS LETRAS 
inv = '' #CRIAÇÃO DE VARIÁVEL VAZIA.
for l in range(len(j)-1, -1, -1):
    inv += j[l]
print(j, inv)