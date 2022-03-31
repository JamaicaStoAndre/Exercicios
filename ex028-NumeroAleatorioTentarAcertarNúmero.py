from random import randint
from time import sleep

n = randint(1, 5)
nr = int(input('Digite um número de 1 a 5 e tente acertar o sorteio: '))
print('Processando...')
sleep(2)
print('-=-'*20)
if nr == n:
    print('Você Acertou! Digitou o número: {} e o número sorteado foi {}'.format(nr, n))
else:
    print('VOCÊ ERROU! O número sorteado foi: {}, e você digitou: {}'.format(n, nr))
print('-=-'*20)