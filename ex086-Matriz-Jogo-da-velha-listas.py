#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-86-matriz-em-python/
#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]#3 linhas começando com 3 números 0, para não precisar ficar colocando append
for l in range(0, 3):# para cada linha "l", percora 3 casas, ou seja, na variável matriz, ele percorre os 3 primeios número, depois o segundo elemento e assim por diante
    for c in range(0, 3):# Dentro de linha ele faz um "for" em coluna "c"
        matriz[l][c] = int(input(f'Digite um valor os valores para: [{l} - {c}]: '))#matriz na linha "l" e na coluna "c"
print(f'Foram digitado : {matriz}')
# O for acima é para armazenar os valores no lugar certo
# O proximo for, serve para printar na tela de modo organizado em forma de matriz
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')# O":^5" serve para exibir um tamanho de 5 caracteres e centralizado. Sem o end, ele vai mostra um abaixo do outro, com end, um ao lado do outro
    print()#Esse print serve para quebrar a coluna sempre que ele terminar as colunas ele, quebra para poder fazer uma linha nova