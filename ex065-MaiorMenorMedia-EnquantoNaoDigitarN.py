r = 's'
maior = menor = iguais = 0
contador = total = 0
while r in 'Ss':
    numero = int(input('Digite um número: '))
    r = str(input('Deseja Continuar (S/N)? '))
    contador += 1
    total += numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        else:
            iguais += 1
print(f'Foram digitados {contador} números. Soma dos números: {total}. A média entre eles é:m {total/contador}')
print('O maior deles é {}, o menor é: {}, tem {} iguais'.format(maior, menor, iguais))
print('FIM')