soma = qtdNr = 0
while True:
    n = int(input('Digite um número ou 999 para parar: '))
    if n == 999:
        break
    soma += n
    qtdNr += 1
print(f'A soma dos {qtdNr} digitados soma os valores de: {soma} ')
print('FIM')