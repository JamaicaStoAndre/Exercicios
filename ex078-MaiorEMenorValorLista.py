listanum = []
menor = 0
maior = 0
for c in range(0, 4): # para 4 número, pois o último é descartado
    listanum.append(int(input(f'Digite um valor para a posição {c} :')))
    if c == 0: #Descobrir qual o maior ou menor valor
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('*-'*20)
print(f'Os valores da listaNum é: {listanum}')
print(f'O maior número digitado foi: {maior}, nas posições: ', end='')
for i, v in enumerate(listanum): #i = índice e v = valor. Enumerate armazenda índice/chave e valor
    if v == maior:# verifica  a chave/índice do maior valor
        print(f'{i} ...', end='')
print(f'\nO menor número digitado foi: {menor}, nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == menor: #verifica o índice/chave do menor valor
        print(f'{i}...', end='')
