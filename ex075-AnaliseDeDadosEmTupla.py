#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/tuplas-em-python/modulos/exercicio-75-analise-de-dados-em-uma-tupla/
num = (int(input('Digite um número: ')), int(input('Digite um número: ')),
       int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'O valor da tupla é: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na posição número: {num.index(3) +1}')# o mais um significa dizer ao usuário que a posição, mas não o local físico dela
else:
    print('O valor 3 não foi digitado pelo usuário')
cont = 0
parece = 0
for n in num:
    if n % 2 == 0:
        pares = (num[cont])
        print(n, end='')
        print(f'Valor de "N": {n}', end='')
        cont += 1
print(f'A tupla com pares é: {pares}')
