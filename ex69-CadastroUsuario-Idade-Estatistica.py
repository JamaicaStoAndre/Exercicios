total = maior18 = totM20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]:')).strip().upper()
    #
    if idade > 18:
        maior18 += 1
    elif idade < 20 and sexo == 'F':
        totM20 += 1
    #
    #
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja Continuar? [S/N]')).strip().upper()
    total += 1
    if resposta == 'N':
        break
print(f'Total: {total}. Maiores de 18 = {maior18}. Mulheres menores de 20: {totM20}')