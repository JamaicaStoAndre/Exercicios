from num2words import num2words
n = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
resposta = ' '
while resposta not in 'Nn':
    nr = int(input('Digite um número entre 0 e 20: '))
    if nr < 0 or nr > 20:
        print('Número inválido')
        #nr = int(input('Digite um número entre 0 e 20: '))
    else:
        num = num2words(nr, lang='pt-br')
        print(num)
        resposta = str(input('Deseja continuar: (S/N): '))
print('Acabou')