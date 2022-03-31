n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = False
while not escolha:
    menu = int(input('Escolha uma das opções abaixo:\n'
                     '[1] - Somar:\n'
                     '[2] - Multiplicar\n'
                     '[3] - Maior\n'
                     '[4] - Novos Número\n'
                     '[5] - Sair do programa'))
    if menu == 1:
        print(f'A soma do número é: {n1 + n2}')
    elif menu == 2:
        print(f'Os dois números multiplicados é: {n1*n2}')
    elif menu == 3:
        if n1 > n2:
            print('O primeiro número é maior')
        elif n1 < n2:
            print('O segundo número é maior.')
        else:
            print('Número iguais')
    elif menu == 4:
        print('Não sei')
    elif menu == 5:
        escolha = True
    else:
        print('Opção inválida, tente novamente.').end = ""
