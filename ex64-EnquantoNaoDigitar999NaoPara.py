n = cont = total = 0
n = int(input('Digite um número e digite 999 para parar: '))
while n != 999:
    total += n
    cont += 1
    n = int(input('Digite um número e digite 999 para parar: '))
print(f'A soma dos {cont} números digitados é: {total}')
