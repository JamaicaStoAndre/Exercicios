frase = str(input('Digite uma frase: ')).upper().strip()#strip elemina todos os espaços antes e depois da frase
#localiza = str(input('Digite a letra a ser procurada: '))
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A letra "A" apareceu a primeira vez na posição: {}'.format(frase.find('A')+1))# o "+1" significa adicionair mais um no dicionairio e vai aumentar em mais um número a posição
print('A última ocorrência da letra A está na posição {}'.format(frase.rfind('A')+1))
