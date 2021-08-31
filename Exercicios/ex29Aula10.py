velocidade = float(input('Qual a velocidade do veiculo no momento(em Km/h)? R:'))

if velocidade > 80:
    print('VOCÊ ESTÁ ACIMA DA VELOCIDADE PERMITIDA (80 Km/h). VOCÊ ESTÁ SENDO MULTADO!!!')
    
    vmulta = (velocidade - 80) * 7 #Calculo do valor da multa.
    
    print('O valor da sua multa é de R${:.2f}.'.format(vmulta)) 

print('DENTRO DA VELOCIDADE PERMITIDA. PARABÉNS!!!')
    
    
