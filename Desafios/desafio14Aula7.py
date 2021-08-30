#-*-coding:utf8;-*-
#qpy:console

c = float(input('Qual a temperatura? (Em graus Celsius) R: '))

#f = (c * 1.8) + 32 #OUTRO TIPO DE CONVERSÃO

f2 = ((9 * c) / 5) + 32

print('A temperatura de {:.0f}°C convertida para Fahrenheit é de {:.1f}°F.'.format(c, f2))