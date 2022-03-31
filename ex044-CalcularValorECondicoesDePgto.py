compras = float(input('Digite o valor das compras: '))
print('''Escolha a forma de pagamento:
[1] À vista dinheiro/Cheque
[2] à vista no cartão 
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    print('O valor de suas compras com 10% de desconto é: {}'.format(compras-(compras * 10 / 100)))
elif opcao == 2:
    print('O valor de suas compras com 5% de desconto é: {}'.format(compras-(compras * 0.5 / 100)))
elif opcao == 3:
    print('O valor de suas compras parceladas em 2x de {}'.format(compras//2))
elif opcao == 4:
    parcela = float(compras+(compras * 20 / 100))
    print('O valor de suas compras parceladas em 3 x ou mais dará um total de {} com parcelas no valor de {}'.format(parcela, parcela //3 ))
else:
    print('Opção inválida, foi compra deu: {}'.format(compras))
