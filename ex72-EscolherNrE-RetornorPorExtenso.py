#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/tuplas-em-python/modulos/exercicio-72-numero-por-extenso/
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'desesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = ' '
while resp not in 'Nn':
        while True:
                num = int(input('Digite um valor entre 0 e 20: '))
                if 0 <= num <= 20:
                        break;
                print('Tente novamente.', end='')
        print(f'Você digitou o número: {cont[num]}')
        resp = str(input('Deseja continuar: (S/N)')).upper().strip()[0]
print('Obrigado e volte sempre!')
