lanche = ('Suco', 'Hambúrguer', 'Pizza', 'Pudim')
print(f'-='*20)
print(f'Este é o Sorted, ele ordena os elementos: {sorted(lanche)}')
print(f'-='*20)
a = (5, 2, 6)
b = (8, 2, 5)
c = a + b
print(f'OBS: existe diferença entre a + b, e b + a, pois quem for declarado primeiro é que terá o valor inicial.')
print(f'Quantas vezes aparece o número 5: {c.count(5)}')
print(f'Index: Em que posição aparece o número 8: {c.index(8)}')
print(f'Index: Procurar um Nr (5), à partir de uma posição(1), ele retorno o número da posição(X).: {c.index(5,1)}, tbm chamdo de deslocamento')
print('-='*20)
pessoa = ('Gustavo', 30, 'M', 99.88)
print(pessoa)
print('É possível apagar a variável a qualquer momento com del')
del(pessoa)
print(pessoa)
