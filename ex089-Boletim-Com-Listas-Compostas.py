#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-89-boletim-com-listas-compostas/
#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.
fichaComBoletim = list()
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2:'))
    media = (nota1 + nota2) / 2
    fichaComBoletim.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar: (S/N) '))
    #
    if resposta in 'Nn':
        break
print('-='*30)
print(f'{"No.:<4"}{"Nome:":<10}{"Média:>8"}')
print(f'-='*30)
for i, a in enumerate(fichaComBoletim):# para cada índice "i" em aluno "a" faça:
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')#exibe o índice"i", aluno:"a[0]"(a na posição zero é o nome) e a média: a[2]:>8.1f ":>8.1f= 8 caracteres, alinhados à direita, com uma casa descimal e ponto flutuante
while True:
    print(f'-='*30)
    opcao = int(input(f'Mostrar notas de qual aluno: (999 para sair): '))
    if opcao == 999:
        print(f'OBRIGADO E VOLTE SEMPRE')
        break
    if opcao <= len(fichaComBoletim) -1:# se a opção escolhida for menor que a quandidade de alunos cadastrados...(o -1 é que descarta o último número)
        print(f'Notas de {fichaComBoletim[opcao][0]} são {fichaComBoletim[opcao][1]}')#{fichaComBoletim[opcao][0]}=Nome, {fichaComBoletim[opcao][1]}= as notas
    print(f'Finalizando')