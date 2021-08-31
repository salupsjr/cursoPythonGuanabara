salario = float(input('Qual o valor do ser salário? R$'))

if salario <= 1250:
    nSalario = salario + (salario * 15/100)
    p = 15
else:
    nSalario = salario + (salario * 10/100)
    p = 10
print('Seu salário de R${:.2f} passa agora a ser de R${:.2f} com {}% de aumento, parabéns!'.format(salario, nSalario, p))