#faça um programa que leia a altura e largura de uma parede em metros, calcule sua área e a
#quantidade de tinta para pitar, sabendo que cada litro de tinta pinta uma área igua a 2m2
n1 = float(input('Qual a altura da parede? '))
n2 = float(input('Qual a largura da parede? '))
print('A parede tem {} metros quadrados, \n e vai precisar de {} litros  de tinta'.format(n1*n2, (n1*n2)/2))
