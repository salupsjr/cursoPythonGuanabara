#-*-coding:utf8;-*-
#qpy:console

#PROGRAMA DE EMPRÉSTIMO PRA FINANCIAMENTO IMOBILIÁRIO.
print('INOVACASA - EMPRÉSTIMO PARA COMPRA DE RESIDÊNCIA')

vCasa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anoPag = int(input('E em quantos anos quer pagar o empréstimo? R:'))

vprestacao = (vCasa / (anoPag*12))

vporcentagem = salario * 30 / 100

if vprestacao > vporcentagem:

   print('O valor da prestação ira exceder mais do que 30% do salário do comprador.\nSalário do Comprador: R${:.2f}.'
         '\nValor do Imóvel: R${:.2f}.\nValor da Parcela: R${:.2f}.\nParecer:Empréstimo Negado.'.format(salario, vCasa, vprestacao))
else: 
   
   print('O valor da prestação não ira exceder mais que 30% do salário do comprador.'
         '\nSalário do Comprador: R${:.2f}.\nValor do Imóvel: R${:.2f}\nValor da Prestação: R${:.2f}.' 
         '\nParecer: EMPRÉSTIMO CONCEDIDO!!'.format(salario, vCasa, vprestacao))   
