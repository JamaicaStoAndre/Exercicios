print('Aluguel de carros\n')
dias = int(input('Digite a quantidade de dias o carro ficou alugado: '))
valorD = float(0.15)
km = float(input('Informe quantos KM foram rodados: '))
print('O valor a pagar pelo aluguel do carro é de R$ {:.2f}'.format((dias*60)+km*0.15))

