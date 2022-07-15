#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-88-palpites-para-a-mega-sena/
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogos = list()# variável que conterá todas as  listas dos Jogos sorteados
listaNumSorteados = list()
print('-='*30)
print(f'         ---JOGO DA MEGA SENA---')
print('-='*30)
quantidadeJogosEscolhido = int(input('Digite a quantidade de Jogos desejado: '))
totalDeJogos = 1#Começa em 1 devido pois se começar em 0 ele fará um número de jogos a mais digitado pelos usuário#Total de vezes que ele vai executar
while totalDeJogos <= quantidadeJogosEscolhido:# Número de jogos da mega sena
    cont = 0#contador de vez quando passar pelo looping
    while True:
        numSorteado = randint(1, 60)
        if numSorteado not in listaNumSorteados:# Se o Número sorteado não estiver na "Lista dos Números sorteados(listaNumSorteados)"
            listaNumSorteados.append(numSorteado)#adiciona o Número sorteado na lista de números sorteados
            cont += 1#adiciona mais um no looping
        if cont >= 6:
            break
    listaNumSorteados.sort()#Coloca os números em ordem crescente
    jogos.append(listaNumSorteados[:])#Cria uma append/cópia "listaNumSorteados[:]" na lista jogos
    listaNumSorteados.clear()#depois de copiar a lista de números sorteados "listaNumSorteados" nós limpamos ela para gerar novos números
    totalDeJogos += 1# para adicionar mais um jogo, até o total escolhido pelo usuário
#print(f'Os números sorteados foram: {jogos}')
#print(f'-=' * 3, f'Sorteando {quantidadeJogosEscolhido}', '-=' * 3)
for i, l in enumerate(jogos):#(ForIt) - Para cada índice "i" na lista "l", neste caso a quandidade de jogos escolhida pelo usário
    print(f'Jogo {i+1}: {l}')# exibe a posiçã índice "i" mais 1, visulamente melhor, e o valor do índice(lista) {l}
    sleep(1)#aguardará 1 seg entre os sorteios