nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print('O nome tem {} letras com espaços'.format(len(nome)))
print('O seu nome sem espaços é {}'.format(len(nome) - nome.count(' ')))
pnome = nome.split()
print('O primeiro nome tem {} letras.'.format(len(pnome[0])))
