#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-87-mais-sobre-matriz-em-python/
### Parte do atual exercício está tudo explicado no ex 086
#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maiorValor = somaCol3 = 0
#as proximas 3 linhas prenchem a matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}-{c}]: '))
print(f'Foram digitados os valores {matriz}')
print('-='*30)
#o Proximo for, exibe de forma correta a matriz na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:#se o elemento que foi exibido na tela for par.
            somaPar += matriz[l][c]
    print()
print('-='*20)
#Primeiro vamos verificar os números pares
print(f'A soma dos valores pares são: {somaPar}')
for l in range(0, 3):# para cada uma das 3 linhas..
    # Para o caso abaixo, a linha está variando"[l]" e a coluna está fixa"[2]"
    somaCol3 += matriz[l][2]# em cada linha na posição 2, pq descarta o último, ou seja, para cada linha da casa 3
print(f'A soma dos valores da coluna 3 é: {somaCol3}')
# esse for abaixo será para a verificação do maior número da linha 2
for c in range(0, 3):#para cada coluna numa range de 0-2
    if c == 0:# se o "c" for igual a 0, quer dizer que é a primeira coluna
        maiorValor = matriz[1][c]# aqui a linha é fixa e a coluna varia
    elif matriz[1][c] > maiorValor:
        maiorValor = matriz[1][c]
print(f'O maior número da linha 2 é: {maiorValor}')
