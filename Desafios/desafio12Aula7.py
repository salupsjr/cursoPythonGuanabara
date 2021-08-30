preco = float(input('Qual o valor do produto? '))

desc = (preco * 5) / 100

precoAtual = preco - desc

print('O desconto é de R${:=.2f} (5% de desconto) e o valor atual é de R${:=.2f}'.format(desc, precoAtual))