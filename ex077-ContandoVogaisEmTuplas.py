palavras = ('Aprender', 'Curso', 'python', 'gratis',
            'curso', 'video', 'programador', 'trabalho')
for p in palavras: # Para cada elemento em Palavra, faça:
    print(f'\n Na palavra {p.upper()} temos:', end='') # Cada vez que começa quebra a linha
    for letra in p: #para elementro dentro de "palavras". (para cada letra na palavra "p":)
            if letra.lower() in 'aeiouáéíóúâêîôû': # Se a letra jogada pra minúscula contiver aeiou:
                print(f'{letra}', end='')
