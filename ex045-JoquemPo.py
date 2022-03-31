from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Escolha suas opções:
        [1] Pedra
        [2] Papel
        [3] Tesoura''')
jogador = int(input('Qual é a sua Jogada: '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Escolha inválida, jogue novamente!!')
else:
    print('-=-'*11)
    print(f'O computador escolheu {itens[computador]}')
    print(f'O Jogador escolheu {itens[jogador]}')
    print('-=-'*11)
    if computador == 0: # Jogou pedra
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('Jogador Venceu!')
        elif jogador == 2:
            print('Computador Venceu')
        else:
            print('Jogada INVÁLIDA!!')
    elif computador == 1: #Jogou papel
        if jogador == 0:
            print('Computador VENCE')
        elif jogador == 1:
            print('EMPATOU')
        elif jogador == 2:
            print('Jogador Vence')
        else:
            print('Jogada INVÁLIDA!!')

    elif computador == 2: #Jogou tesoura
        if jogador == 0:
            print('Jogador VENCEU')
        elif jogador == 1:
            print('Computador VENCEU')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('Jogada INVÁLIDA!!')
