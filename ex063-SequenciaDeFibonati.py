print('=*' *15)
print('Sequencia de Fibonacci')
print('=*' *15)
n = int(input('Digite a quantidade de termos que deseja imprimir: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2} ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> Fim')



'''print('~'*30)
print('Sequencia de fibonacci')
print('~'*30)
n = int(input('Digite quantos termos deseja imprimir: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> Fim')'''

