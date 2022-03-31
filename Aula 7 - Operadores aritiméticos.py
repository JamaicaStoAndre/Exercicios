n2 = int(input('Digite um número: '))
n1 = int(input('Digite outro número: '))
soma = n1+n2
divisao = n1//n2
mult = n1*n2
expon = n1**n2
resto = n1%n2
print('O resultado da soma é {}, \n da divisão é {} \n e da multiplicação é {}'.format(soma, divisao, mult), end=' ')
print('O resultado da exponenciação é {}, \n e o resto da divisão é {}'.format(expon, resto))
