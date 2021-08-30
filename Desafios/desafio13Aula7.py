salario = float(input('Qual o salário do funcionário? '))

salarioAtual = salario + (salario * 0.15)

print('O salário com 15% de aumento ficou no valor de R${:=.2f}'.format(salarioAtual))