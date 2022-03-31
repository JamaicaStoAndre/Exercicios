from datetime import date
anoAtual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = anoAtual - nascimento
if idade <= 9:
    print('Você tem {} anos e é da categoria Mirim'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e é da categoria INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e é da categoria Júnior '.format(idade))
elif idade > 19 and idade <= 25:
    print('Você tem {} anos e é da categoria Sênior '.format(idade))
else:
    print('Você tem {} anos e é da categoria Master '.format(idade))