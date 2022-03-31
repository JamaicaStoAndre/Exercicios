i = int(input('Digite um número de início: '))
f = int(input('Digite um número final: '))
p = int(input('Digite o número de passos: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print(f'A soma dos número é {s}')