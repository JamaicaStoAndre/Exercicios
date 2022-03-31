print('Gerador de PA')
print('-=-' * 20)
primeiro = int(input('Digite o primeiro número: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} ', end='')
    termo += razao
    cont += 1
print('FIM')