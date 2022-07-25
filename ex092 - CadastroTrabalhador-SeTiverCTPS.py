#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/dicionarios-em-python/modulos/exercicio-92-cadastro-de-trabalhador-em-python/
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
dados['nasc'] = int(input('Digite o ano de nascimento: '))
dados['idade'] = datetime.now().year - dados['nasc']
dados['ctps'] = int(input('Carteira de trabalho: 0 para quando não tiver: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o valor do salário : R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print(dados)
print('-='*30)
for k, v in dados.items():# para cada elemento em chave e valor
    print(f'O {k} tem o valor {v}')
