#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/dicionarios-em-python/modulos/exercicio-94-unindo-dicionarios-e-listas/
#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoa = {}
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print(f'Erro digite M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Deseja continuar? (S/N)')).upper()[0]
        if resposta in 'SN':
            break
        print(f'ERRO! Responda apenas S ou N ')
    if resposta == 'N':
        break
print('-='*30)
print(galera)
print('-='*30)
print('A) Quantas pessoas foram cadastradas?')
print(f'Ao todo foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'B) A média de idade: {media:5.2f} anos')#5 casas ao todo, 2 números decimais em float
print('-='*30)
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:#para cada pessoa em galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<< ENCERRADO >>')