soma = 0
cont = 0
for c in range(1,7):
        nr = int(input('Digite os números: '))
        if nr % 2 == 0:
            soma += nr
            cont += 1
        print(f'Vocẽ informou: {cont} números PARES, e a soma foi: {soma}')

