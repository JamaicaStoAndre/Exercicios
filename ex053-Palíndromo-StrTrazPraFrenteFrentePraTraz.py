frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1] #Regra de fatiamento, não precisa nesse caso do for. [::-1] = pega a primeira posição, a última e comaça de traz pra frente.
#print(junto)
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('Temos um palindromo!!')
else:
    print('Não temos um palíndromo')
print(f'A frase normal: {frase}.')
print(f'A frase invertida: {inverso}')