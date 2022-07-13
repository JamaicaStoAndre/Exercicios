#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-83-validando-expressoes-matematicas/
# Crie um programa onde o usuário digite uma expressão  qualquer
#que use parênteses.Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta e se o mesmo
# de parentes abrindo e fechando
expressao = str(input('Digite uma expressão matemática: '))
pilha = []
for simb  in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Sua expresão é válida:')
else:
    print(f'Sua expressão é inválida')
