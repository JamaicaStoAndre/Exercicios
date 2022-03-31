from datetime import date
nrMaiores = 0
nrMenores = 0
for c in range(1,8):
    nascimento = int(input(f'Digite o ano em que a {c}º nasceu? : '))
    anoAtual = date.today().year
    idade = anoAtual - nascimento
    if idade > 21:
        #print('Essa pessoa é maior de idade')
        nrMaiores += 1
    else:
        #print('Essa pessoa não é maior de idade.')
        nrMenores += 1
print(f'São {nrMaiores} maiores de idade e {nrMenores} menores de idade. ')

