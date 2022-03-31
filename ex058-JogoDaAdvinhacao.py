'''from random import randint
from time import sleep
cont = 1
print('Sou seu computador, tente advinhar o núrmero....')
sleep(1)
nr = int(input('Digite o número entre 1 e 10 para sorteio: '))
n = randint(1, 11)
print('Sorteando..')
sleep(1)
while nr != n:
    #nr = int(input('Digite um número para sorteio'))
    if nr < n:
        nr = int(input(('O número digitado é menor que o sorteado, tente outro:  ')))
        cont += 1
    else:
        nr = int(input(('O número digitado é maior que o nr sorteado, tente outro: ')))
        cont += 1
print(f'Parabéns, você acerto o número sorteado {n} em {cont} tentativas.')'''

#Solução do Guanabara abaixo:
from random import randint
computador = randint(1, 10)
print(' Sou seu computador, vou pensar em um número de 0 a 10... ')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Seu número é menor, tente mais uma vez')
        elif jogador > computador:
            print('Seu número é maior que o sorteado, tente novamente.')
print(f'Você acertou!! com {palpites} tentativas.')


