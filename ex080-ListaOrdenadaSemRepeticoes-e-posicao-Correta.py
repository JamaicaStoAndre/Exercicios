# Em qual posição adicionar o número digitado
#Nós teremos somente 3 possibilidades: 1 - Ou é o primeiro nr da lista(vai dar um apend),
# 2 - ou ele é último valor da lista(vai dar um apend tbm)
# ou ele está no meio
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:# vou dar um append, se o ele for o primeiro "c == 0" ou se for mair que o úlitmo "or n > lista[-1]. lista[-1]=último elemento "
        lista.append(n)
    else:
        pos = 0# posição "pos"
        while pos < len(lista):# vai varrer da posição 0 até a última posição
            if n <= lista[pos]:#verificar dentro de cada posição se o número é menor ou igual a ele, se for ele insere numa posição específica
                lista.insert(pos, n)# insere na lista " lista.insert" na posição "pos" o valor digitado "n"
                break# não será mais preciso o looping pois será inserido só uma vez
            pos += 1
print(f'-='*20)
print(f'Os valores digitados em ordem crescente são: {lista}')
