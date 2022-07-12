num = [2, 3, 7, 9, 3, 7]
print(f'Mostrar o valor da lista: {num}')
num[2] = 3
print(f'Acrescentar o valor 3 na posição 2: {num}')
num.append(7)
print(f'Acrescentar o valor 7 no final da lista com append {num}')
num.sort()
print(f'Colocar em ordem crescente com sorte {num}')
num.sort(reverse=True)
print(f'Colocar em ordem inversa: {num}')
num.insert(2, 0)
print(f'Colocar o valor 0 na posição 2 com insert: {num}')
print(f'Saber o tamanho da lista: {len(num)}')
num.remove(2)
print(f'Remove o "primeiro" elemento que conter o nr 2 com remove: {num}')
if 9 in num:# se existir o nr 4 ele vai remover, se não, ele dará a msg abaixo
    print(f'Removendo o 9')
    num.remove(9)
else:
    print(f'O número 9 não existe na lista, usando o remove, se não fizer o laço, vai dar erro se não encontrar o 4')
print('-='*30)
valores = []
valores.append(4)
valores.append(6)
valores.append(9)
valores.append(2)
print(f'O valor da lista é: {valores}')
for c in valores:
    print(f'Os valores com append é: {c}')
print(f'\nExibindo chave e valor com enumerate')
for c, v in enumerate(valores): # para cada elemento "c" grava o valor "v" com enumerate.
    print(f'Na posição: {c}, temos os valores {v}')
print(f'Fim da lista')
print(f'=-'*20)
print('Outra peculiaridade do Python: união de listar')
a = [1, 4, 6, 7]
b = a
print(f'O valor da lista de B é {b}')
print(f'O valor da lista de A é {a}')
b[2] = 8 # neste caso, irá sobrescrever tbm a lista "A" pq o Python faz uma ligação entre elas
print(f'A nova lista na posição 2 é {a}')
print(f'Para criar uma cópia para que não sejam alterardos os valores de "a". Ex. b = a[:]')
b = a[:]
b[2] = 20
print(f'O valor da lista de A é {a}')
print(f'O valor da lista de B é {b}, agora foi alterado o valor de B, sem alterar o valor de "a"')
print(f'')
print(f'=-'*20)
novosValores = []
print(f'Inserindo dentro de listas com Laço For')
for cont in range(0, 2):
    novosValores.append(int(input('Digite um valor para inserir na lista: ')))
print(f'Os valores digitados acima são: {novosValores}')
