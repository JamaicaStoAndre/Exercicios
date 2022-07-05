#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/tuplas-em-python/modulos/exercicio-74-maior-e-menor-valores-em-tupla/
import random
from random import randint
print('-='*20)
numeros = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50))# repete 5 vezes o sorteio e armazena na tupla
print(f'O resultado da duplas com os valores é: {numeros}')
print('-='*20)
print('Outra maneira de fazer:')
print('Os valores sorteados foram: ', end='')#end é para não pular de linha
for n in numeros: #para cada elemento ("n") em números...
    print(f'{n} ', end='')
print('-='*20)
print('Maior e menor números..')
print(f'O maior número da tupla é: {max(numeros)}')
print(f'O Menor número da tupla é: {min(numeros)}')
