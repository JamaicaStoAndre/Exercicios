print('Gerador de PA')
print('-=-' * 20)
primeiro = int(input('Digite o primeiro número: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostra mais? Ou 0 para sair: '))
print(f'Progressão finalizada com sucesso com {total} de termos mostrados ')
