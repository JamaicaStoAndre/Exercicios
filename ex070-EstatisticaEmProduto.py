#Link da aula: https://www.cursoemvideo.com/curso/python-3-mundo-2/aulas/repeticoes-em-python-while/modulos/exercicio-70-estatisticas-em-produtos/
print('-'*20)
total = prodMaior = prodMaisBarato = cont = 0
nomeProdMaisBarato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: '))
    total += preco
    cont += 1
    if cont == 1 or preco < prodMaisBarato:
        prodMaisBarato = preco
        nomeProdMaisBarato = produto
    if preco > 1000:
        prodMaior += 1
   #
    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R${total} ;')
print(f'Tem {prodMaior} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {nomeProdMaisBarato}  que custa R${prodMaisBarato}')
print('-='*20)

