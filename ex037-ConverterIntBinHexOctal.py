n1 = int(input('Digite um número inteiro para converter: '))
pergunta = int(input('''Qual a base que você deseja converter: 
            [1] Binário
            [2] Octal
            [3] Hexadecimal\n'''))
#binario = bin(n1)
if pergunta == 1:
    print('O número digitado foi {} e o mesmo convertido em binário é: {}'.format(n1, bin(n1)[2:]))
elif pergunta == 2:
    print('O número {}, convertido para Octal é: {}'.format(n1, oct(n1)[2:]))
elif pergunta == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(n1, hex(n1)[2:])) #[:2] quer dizer para pegar a partir da segunda posição da resposta
else:
    print('Opção inválida, rode o programa novamente!!')
