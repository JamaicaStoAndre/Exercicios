n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
print('O maior valor é: {} e o menor valor é: {}'.format(maior, menor))
