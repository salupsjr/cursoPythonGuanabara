#-*-coding:utf8;-*-
#qpy:console


print('-=' * 20)
print('CALCULO DE MASSA CORPÓREAS - IMC')
print('-=' * 20)

peso = float(input('Digite seu peso [ex: 120.5]: '))
altura = float(input('Digite sua altura [ex: 1.86]: '))

imc = peso / (altura*altura)

if imc < 18.5: 
   print('O seu IMC é de {:.2f} e você está ABAIXO DO PESO.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('O seu IMC é  de {:.2f} e você está NORMAL.'.format(imc))
elif imc >= 25 and imc < 30:
    print('O seu IMC é de {:.2f} e você está com SOBREPESO.'.format(imc))
elif imc >= 30 and imc <= 40:
    print('O seu IMC é de {:.2f} e você está em OBESIDADE.'.format(imc))
else:
   print('O seu IMC é de {:.2f} e você está em OBESIDADE MÓRBIDA. CUIDADO!!!'.format(imc))