#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-84-lista-composta-e-analise-de-dados/
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves.
listaTemporaria = []
listaPrincipal = []
maiorPeso = menorPeso = 0
while True:
    listaTemporaria.append(str(input('Digite um nome: ')))
    listaTemporaria.append(float(input('Digite o peso: ')))
    if len(listaPrincipal) == 0:# Se lista pcp não foi preenchida ainda.
        maiorPeso = menorPeso = listaTemporaria[1]# então maiorPeso, menor peso é igua a lista temporária na posição 1(peso)
    else:# caso não seja o primeiro registro...
        if listaTemporaria[1] > maiorPeso:
            maiorPeso = listaTemporaria[1]
        if listaTemporaria[1] < menorPeso:
            menorPeso = listaTemporaria[1]
    listaPrincipal.append(listaTemporaria[:])# Esta lista principal, está criando uma cópia da lista temporária. Podendo assim alterar o valor sem alterar a lista temporária.
    listaTemporaria.clear()# Remova pra ver o feito, as listas ficam erras.
    #
    resposta = (str(input('Deseja continuar? (S/N)')))
    if resposta in 'Nn':
        break
print(f'-='*30)
print(f'Esta é a lista TEMPORÁRIA: {listaTemporaria}')
print(f'Esta é a lista PRINCIPAL: {listaPrincipal}')
print(f'Foram cadastradas {len(listaPrincipal)} pessoas. ')
print(f'Maior peso: {maiorPeso} de nome:', end='')
for p in listaPrincipal: #ForIt = para cada elemento. Ou seja, para cada elemento ele vai varrer a lista. Para cada pessoa "p" na lista principal. Vai pegar cada lista e jogar em 'p'
    if p[1] == maiorPeso:# se pessoa na posição 1 = peso...
        print(f'[{p[0]}] ', end='')# Vai exibir o nome da pessoa "p[0]" que tem o mario peso
print()
print(f'Menor peos: {menorPeso} e foi a pessoa ', end='')
for p in listaPrincipal:
    if p[1] == menorPeso:
        print(f'[{p[0]}]', end='')
print()
