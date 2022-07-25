#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/dicionarios-em-python/modulos/exercicio-91-jogo-de-dados-em-python/
#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter# biblioteca de ordenação.
dados = {'Jogador-1': randint(1, 6),
         'Jogador-2': randint(1, 6),
         'Jogador-3': randint(1, 6),
         'Jogador-4': randint(1, 6)}
print(f'Valores sorteados:')
ranking = list()
for k, v in dados.items():
    print(f'O {dados[k]} tirou o número {v} ')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)#"Sorted = ordenar. "key=itemgetter(1)" = faz com que seja ordenado pela chave número 1, neste caso, o número sorteado pelo randint e se fosse 0, ordenaria pelos Jogadores."reverse=True" = ordena em ordem decrescente
print('-='*30)
print(f' ==  JOGO DE DADOS == ')
for i, v in enumerate(ranking):
    print(f'O {i+1}º Colocado foi {v[0]} com o número: {v[1]}')
    sleep(1)
