#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/dicionarios-em-python/modulos/exercicio-90-dicionario-em-python/
#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média do aluno: {aluno["nome"]} '))
if aluno['media'] >= 7:
    aluno['situacao'] = str('Aprovado')
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = str('Em Recuperação!')
else:
    aluno['situacao'] = str('Reprovado!')
for k, v in aluno.items():
    print(f'Função utilizando ".itens": - {k} é igual a {v}')
print('-='*30)
print(f'O aluno {aluno["nome"]} está: {aluno["situacao"]}')
print('-='*30)
print(aluno)
