numero = list()
while True: # enquando não encontrar o break:
    n = int(input(f'Digite um valor: '))
# Se o valor digitado "n" não estiver na lista, ele adiciona
    if n not in numero:
        numero.append(n)
        print(f'Valor adicionaodo com sucesso')
# Se já existir na lista ele não deixa adicionar
    else:
        print(f'Valor duplicado. Não foi adicionado')
    resposta = str(input('Deseja continuar? (S/N)')).upper()
    if resposta in 'Nn':
        break
print('=-'*20)
print(f'Os valores digitados foram: {numero}')
numero.sort()# Coloca números em ordem crescente
print(f'Os valores em ordem crescente são {numero}')