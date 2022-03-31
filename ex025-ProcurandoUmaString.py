nome = str(input('Digite seu nome: '))
if nome.find('Souza') == -1 :
    print(nome, ': Não contém Souza')
else:
    print(nome, ': Contém souza')
nome = str(input('Digite seu nome: '))
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

