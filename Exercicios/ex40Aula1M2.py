from typing import ForwardRef


nota1 = float(input('Digite a nota da AV1: '))
nota2 = float(input('Digite a nota da AV2: '))
media = (nota1 + nota2)/2

if media <= 4.9:
      print('A média entre {:.1F} e {:.1F} é de {:.1F} e o aluno está REPROVADO.'.format(nota1, nota2, media))
elif media >= 5 and media <= 6.9:
      print('A média entre {:.1F} e {:.1F} é de {:.1F} e o aluno está em RECUPERAÇÃO.'.format(nota1, nota2, media))
else:
      print('A média entre {:.1F} e {:.1F} é de {:.1F} e o aluno está APROVADO. PARABÉNS!!'.format(nota1, nota2, media))