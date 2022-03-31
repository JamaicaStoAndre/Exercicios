cidade = str(input('Digite um nome de cidade: ')).strip() #remove os espaços
#print(cidade[:5].upper() == 'SANTO')
if cidade[:5].upper() == 'SANTO' :
    print('É igual a Santo')
else:
    print('Não é igual a santo')
