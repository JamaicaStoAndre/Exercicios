n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro múmero {} é maior que o segundo número {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número {} é maior que o primeiro número {}'.format(n2, n1))
else:
    print('Os número são iguais')
