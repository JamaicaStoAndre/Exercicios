dist = float(input('Digite a quantidade de KM: '))
if dist <= 200:
    print('Você vai pagar pela sua viagem: R$ {:.2f}'.format(dist*0.5))
else:
    print('Você vai pagar por sua viagem: R$ {}'. format(dist*0.45))
