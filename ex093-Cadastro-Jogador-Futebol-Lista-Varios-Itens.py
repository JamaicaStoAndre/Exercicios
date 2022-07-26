#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/dicionarios-em-python/modulos/exercicio-93-cadastro-de-jogador-de-futebol/
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = list()
jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['Total_de_partidas'] = int(input(f'Quantas partidas o jogador {jogador["nome"]}: '))
for c in range(0, jogador['Total_de_partidas']):
    partidas.append(int(input(f'Quantos gol {jogador["nome"]} fez na partida {c}?: ')))
jogador['Total_de_gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('-='*30)
print(f'Duas formas de exibir os dados')
print('-='*30)
for k, v in jogador.items():
    print(f'-> A chave {k} tem o valor: {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} fez {len(jogador["Total_de_gols"])} gols.')#poderia ter sido usado o total de partidas, mas foi usado o len() como exemplo
for i, v in enumerate(jogador['Total_de_gols']):
    print(f'    => na partida {i} o jogador {jogador["nome"]} fez {v} gols.')
print(f'o Jogador {jogador["nome"]} fez {jogador["total"]} gols')
