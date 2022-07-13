#Primeiro exemplo: uma lista dentro de outra, mas quando altera a segunda lista, vai alterar a primeira lista
teste = list()
teste.append('Gustabo')
teste.append(40)
galera = list()
#galera.append(teste)# neste momento estou colocando teste dentro de galera, quando mudar uma estrutura a outra vai mudar tbm
galera.append(teste[:])# o "[:]" vai fazer uma cópia
teste[0] = 'Maria'
teste[1] = '22'
#galera.append(teste)# neste caso ele criou mais um local na memória com novos valores de teste
galera.append(teste[:])# "[:]"irá fazer uma cópia e inserir os novos valores no outro campo da memória
print(galera)
print('-='*30)
galera = [['João', 42], ['Maria', 45], ['Pedro', 12], ['Alan', 40]]
print(galera)
print(f'Exibi galera na posição 0 e exibe o íten 0 tbm  galera[0][0]: {galera[0][0]}')#
print(f'Exibi galera na posição 2 e exibe o íten 1 tbm  galera[2][1]: {galera[2][1]}')#
print('-='*20)#
print('Imprimindo os nomes com FOR')
for p in galera:# Para cada pessoal em galera...faça
    print(p, end='')
    print()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('-='*20)
pessoas = list()
dados = list()
#
#O bloco abaixo serve para ler os dados(informação auxiliar) e jogar dentro de pessoas(variável final) e apagar os dados no final
for c in range(0, 3):# rang de 4 loopings
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Digite a idade: ')))
    pessoas.append(dados[:])# cria uma cópia de "dados" dentro de "pessoas"
    dados.clear()#limpa a variável "dados"
print(pessoas)
print('-='*20)
maiorIdade = menorIdade = 0
print('Filtrando por idade')
for p in pessoas:# para cada pessoa em "pessoas", faça:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maiorIdade += 1
    else:
        print(f'{p[0]}, é menor de idade')
        menorIdade += 1
print(f' Existem {maiorIdade} maior de 21 anos e {menorIdade} menores de 21 anos')
