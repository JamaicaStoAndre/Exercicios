#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-81-extraindo-dados-de-uma-lista/
#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
## A) Quantos números foram digitados
## B) A lista de valores, ordenada de forma decrescente
## C) Se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))#apend vai colocar sempre no final do índice
    resposta = str(input('Deseja continuar? (S/N): '))
    if resposta in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} números')
valores.sort(reverse=True)# sort =  colcar em ordem crescente. ".sort(reverse=True)" = coloca em ordem inversa
print(f'Os valores digitados em ordem inversa é: {valores}')
#
##Verifica se um número existe na lista:
if 5 in valores: # se é um valor fixo, não tem necessidade de fazer laço, pode ser usado o "in" do python. Pode ser tuplas, listas, dicionaário, etc
    print(f'Os valor 5 faz parte da lista. ')
else:
    print(f'O valor 5 não foi encontrado.')
