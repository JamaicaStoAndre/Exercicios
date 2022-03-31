from datetime import date
genero = str(input('Digite M se você é mulher ou H se você é Homem: ')).upper()
if genero == 'M':
    print('Você não precisa de alistamento militar!!')
elif genero == 'H':
    anoNascimento = int(input('Digite o ano de seu nascimento: '))
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    if idade < 18:
        saldo = idade - 18
        print('Você tem {} anos ainda não precisa se alistar'.format(idade))
        print('Seu alistamento é em {}'.format(anoAtual - saldo))
    elif idade == 18:
        print('Você precisa se alistar este ano')
    else:
        saldo = idade - 18
        ano = anoAtual - saldo
        print('Você tem {} anos, deveria ter se alistado em: {}'.format(idade, ano))
else:
    print('Gênero não reconhecido')