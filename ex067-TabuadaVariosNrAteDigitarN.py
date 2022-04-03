while True:
    nr = int(input('Digite a tabuada que deseja ver: '))
    for c in range(1, 11):
        print(f'{nr} X {c} = {nr*c}')
        c += 1
    resposta = str(input('Deseja continuar (S/N): '))
    if resposta in 'Nn':
        print('Obrigado e volte sempre!!')
        break


