num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m', end='')
        tot += 1
    else:
        print(f'\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[m O número {num} foi divisível {tot} vezes.')
if tot == 2:
    print(f'O número {num} é um número primo.')
else:
    print(f'O número {num} não é um número primo.')