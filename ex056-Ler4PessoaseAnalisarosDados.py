somaidade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeDoMaisVelho = ''
totMulher = 0
for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}º pessoa: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M / F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeDoMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeDoMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher += +1
mediaIdade = somaidade / 4
print(f'A média da idade do grupo é: {mediaIdade}')
print(f'O nome do homem mais velho é: {nomeDoMaisVelho} e tem {maiorIdadeHomem} anos.')
print(f'Existem {totMulher} mulher com menos de 20 anos.')