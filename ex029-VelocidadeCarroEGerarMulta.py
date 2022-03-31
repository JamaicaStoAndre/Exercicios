vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Você ultrapassou o limite de velocidade')
    print('Você levou uma multa de R${:.2f}'.format((vel-80)*7))
else:
    print('Velocidade dentro dos limites')
