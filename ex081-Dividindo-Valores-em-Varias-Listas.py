#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-82-dividindo-valores-em-varias-listas/
#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, # respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
pares = []
inpares = []
while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = str(input('Deseja continuar? (S/N): '))
    pos = 0
    if pergunta in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        inpares.append(v)
print('+='*20)
print(f'Os valores pares são: {pares}')
print(f'Os valores ímpares pares são: {inpares}')
print(f'O valor digitado foi {lista}')


