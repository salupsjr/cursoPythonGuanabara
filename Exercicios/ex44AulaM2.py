'''#MINHA RESOLUÇÃO
preço = float(input('Qual o valor da compra? R$'))
print('QUAL A FORMA DE PAGAMENTO? \n[1] À VISTA(DINHEIRO OU CHEQUE)\n[2] Á VISTA NO CARTÃO \n[3] EM ATÉ 2X NO CARTÃO\n[4] EM 3X OU MAIS NO CARTÃO')
opção = int(input('OPÇÃO:'))

if opção == 1:
    preçoA = preço - (preço*10/100)
    print('O valor da compra terá 10% de desconto. \nO valor com desconto é de R${:.2f}.'.format(preçoA))
elif opção == 2:
    preçoA = preço - (preço*5/100)
    print('O valor da compra terá 5% de desconto. \nO valor da compra com desconto é de R${:.2f}'.format(preçoA))
elif opção == 3:
    print('O valor da compra será de R${:.2f}'.format(preço))
elif opção == 4: 
    preçoA = preço + (preço*20/100)
    print('O valor total da compra parcelada será de R${:.2f}'.format(preçoA))
else:
    print('Opção inválida!')'''

#RESOLUÇÃO GUANABARA

print('{:=^40}'.format(' Lojas Lorenna '))
preço = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À VISTA (COM 20% DE DESCONTO)
[2] À VISTA NO CARTÃO (COM 5% DE DESCONTO)
[3] EM 2X NO CARTÃO (SEM DESCONTO)
[4] EM 3X NO CARTÃO (COM JUROS)''')
opção = int(input('Qual a opção? R:'))

if opção == 1:
    total  = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4: 
    total = preço + (preço * 20 / 100)
    totParc = int(input('Quantas parcelas? [até 10x]: '))
    parcela = total / totParc
    print('Sua compra será parcelada em {}x e o valor de cada parcela é R${:.2f}'.format(totParc, parcela))
else:
    print('OPÇÃO INVÁLIDA!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no total.'.format(preço, total))
