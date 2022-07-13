#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-85-listas-com-pares-e-impares/
#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os
# valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
#
número = [[], []]# Uma variável com uma lista, onde a mesma tem duas listas dentro.Para este exercício a lista da esquerda são com os pares e o da direitra são os ímpares
valor = 0# Este valor é utilizado como variável temporária, para armazenar o valor que o usuário digita, após isso tratar e enviar para o local correto
for c in range(0, 7):
    valor = int(input(f'Digite um valor para a posição {c}: '))
    if valor % 2 == 0:
        número[0].append(valor)# o append adiciona em elemento com (valor) em na variável número, na posição "0"(pares)
    else:# se não ele é ímpar
        número[1].append(valor)
print(f'-='*30)
#Colocando os valores em ordem descrescente com .sort
número[0].sort()
número[1].sort()
print(f'Os valores digitados foram: {número}. \nOs pares são {número[0]}.\nÍmpares são {número[1]}')
