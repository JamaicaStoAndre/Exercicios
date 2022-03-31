#Faça um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 6.117 e mostrar6
'''from math import trunc
n1 = float(input('Digite um número com casas decimais: '))
print('O número arredondado é: {}'.format(trunc(n1)))'''
n1 = float(input('Digite um número com casas decimais: '))
print('O número digitado foi {} e sua parte inteira é {}'.format(n1, int(n1)))

