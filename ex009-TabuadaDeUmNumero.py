#Exer 5 - Faça um programa que leia um número qualquer e mostre sua tabuada
n1 = int(input('Digite um número: '))
n2 = 1
print(20*'=')
for i in range(10):
    print('{} x {:2} = {:>2}'.format(n1, n2, n1*n2))
    n2 += 1
print(20*'=')