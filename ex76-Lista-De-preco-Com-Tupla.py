#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/tuplas-em-python/modulos/exercicio-76-lista-de-precos-com-tupla/
listagem = ('Leite', 4.56,
            'Café', 19.50,
            'Presunto', 7.8,
            'Pizza', 20.5,
            'Picanha', 48.8,
            'Pão', 5.8,
            'Banana', 5.5)
print('-'*40)
print(F'{"LISTAGEM DE PREÇOS":^40}')# "^" = Centralizado e "40" = 40 cacarteres
print(f'-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0: #neste caso ele percore, um a um, as segunda coluna é a par
        print(f'{listagem[pos]:.<30}',end='')# :.< = Formatação: Completar com "." alinhados à esquerda "<". 30 = é igual ao total de caracteres na impressão
    else: #Se não for a condição acima, então a coluna exibida será preço
        print(f'R$ {listagem[pos]:>8.2f}')# :>8 = Alinhamento a direita 15px. 2f é a casa decimal
print('Volte sempre!')
