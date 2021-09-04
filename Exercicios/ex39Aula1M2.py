from datetime import date
anoNasc = int(input('Digite sua data de nascimento: '))
sexo = str(input('Qual seu sexo: [M - MASCULINO ou F - FEMININO] ')).upper().strip()

anoAtual = date.today().year #ano atual do sistema

idade = anoAtual - anoNasc

tempo1 = anoNasc - anoAtual + 18

tempo2 = idade - 18

if sexo == 'F':
      print('Você não tem obrigação militar.')
else:
      if idade < 18:
            print('Você tem ou completará {} anos e deve se alistar daqui há {} ano(s).'.format(idade, tempo1))
      elif idade == 18:
            print('Você tem ou completará {} anos este ano. Deverá se alistar IMEDIATAMETE!'.format(idade))
      else:
            print('Você tem ou completará {} anos e já passou do prazo de alistamento há {} ano(s).'.format(idade, tempo2 ))
