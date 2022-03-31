# Ex2 - Faça um algorítimo que leia um número e mostre na tela seu sobro, tripo e sua raiz quadrada
n1 = int(input('Digite um número: '))
print('O dobro de {} é {}, \n seu tripo é {}, e sua raiz quadrada é {:.2f}'.format(n1, n1*2, n1*3, pow(n1, (1/2))))
