from calendar import isleap
ano = int(input('Digite um ano qualquer com 4 digitos: '))
if isleap(ano):
    #print('O ano é bissexto')
    print(isleap(ano))
else:
    #print('Não é bissexto')
    print(isleap(ano))

