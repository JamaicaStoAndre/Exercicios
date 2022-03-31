altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura **2)
print('Seu IMC é {:.1f}, você está: '.format(imc),end='')
if imc <= 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')