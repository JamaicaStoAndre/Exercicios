from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(1, 11)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
            tipo = str(input('Você deseja par ou impar: (P/I): ')).upper().strip()[0]
    print(f'Você jogou {jogador}, o computador jogou {computador} e a soma é {soma}')
    print('Deu par' if soma % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você ganhou')
            v += 1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if soma % 2 == 1:
            print('Você ganhou')
            v += 1
        else:
            print('Você perdeu Jogador!')
            break
    print('Vamos Jogar novamente: ')
print(f'Você ganhou {v} vezes')






'''from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 11)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você deseja Par ou impar: (P/I): ')).strip().upper()[0]
    print(f'Você Jogou: {jogador}, o computador jogou: {computador}. A soma é {soma}')
    print('Deu par' if soma % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu!!')
            v += 1
        else:
            print('Você perdeu!!')
            break
    elif tipo == 'I':
        if soma % 2 ==1:
            print('Você venceu!!')
            v += 1
            break
    print('Vamos jogar novamente? ')
print(f'Você venceu {v} vezes.')
'''



'''from random import choice
import random
ganho = 's'
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    print('-='*20)
    n = int(input('Digite um número: '))
    r = str(input('Você deseja par ou ímpar? (P/I): ')).upper().strip()
    escolhido = random.choice(lista)
    soma = n + escolhido
    print(f'O conputador escolheu: {escolhido}')
    if soma % 2 == 0:
        resposta = 'P'
        print(f'{soma} é par')
    else:
        resposta = 'I'
        print(f'{soma} é Impar')
    if resposta == r:
        print(f'Você ganhou deu {resposta}')
    else:
        print(f'Deu {resposta}, você perdeu!')
        break
print('=-'*20)'''