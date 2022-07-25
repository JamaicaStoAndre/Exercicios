#https://www.youtube.com/channel/UCrWvhVmt0Qac3HgsjQK62FQ
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 45}
print(f'Exibindo todo conteúdo da lista: {pessoas}')
print(f'Imprimindo chaves: {pessoas.keys()}')
print(f'Exibindo os valores: {pessoas.values()}')
print(f'Exibindo os ítens da lista: {pessoas.items()}')
print('-='*30)
#laço para exibir os dados
print(f'Laço para exibir os dados')
for k in pessoas.keys():#para cada chave "keys" 'k' em pessoas:
    print(f'{k}')
print('-='*30)
print(f'Exibindo os valores')
for k in pessoas.values():#vai mostrar só os valores do Dicionáio
    print(k)
print('-='*30)
print(f'Exibindo tos os Ítens')
for k, v in pessoas.items():#Exibe os ítens dentro de chave e valor. Tupas e listas usam enumerate
    print(f'{k} = {v}')
print('-='*30)
print(f'Alterando os dados de um dicionário')
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():#Exibe os ítens dentro de chave e valor. Tupas e listas usam enumerate
    print(f'{k} = {v}')
print('-='*30)
print(f'Deletando dados do dicionário')
del pessoas['sexo']
for k, v in pessoas.items():#Exibe os ítens dentro de chave e valor. Tupas e listas usam enumerate
    print(f'{k} = {v}')
print('-='*30)
print(f'Inserindo novos elementos no dicionário')
pessoas['peso'] = 88.9
for k, v in pessoas.items():#Exibe os ítens dentro de chave e valor. Tupas e listas usam enumerate
    print(f'{k} = {v}')
print(f'-='*20)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())#aqui estamos criando uma cópia "copy", se fosse uma lista faríamos "[:]"
for e in brasil:# For para cada elemento em Brasil 'e'
    for v in e.values():# Para cada valor em elementos (e.values irá exibir o valor de cada elemento)
        print(f'{v}', end=' ')
    print()#quebrar a linha
