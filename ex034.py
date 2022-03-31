salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    salario += 1.1
else:
    salario += 1.15
print('Seu salario com aumento ficou em: R${}'.format(salario))
