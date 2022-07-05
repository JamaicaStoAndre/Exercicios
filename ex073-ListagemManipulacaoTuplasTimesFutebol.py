times = ('Corintians', 'Cruzeiro', 'vasco', 'flamento', 'sao paulo', 'palmeiras', 'Chapecoense', 'Atletico mineiro', 'Atletico Goias',
         'Avaí', 'Figueirense', 'Joinvile', 'Criciúma')
print(f'Os cinco primeiros times da lista são: {times[0:5]}')
print('...'*20)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('...'*20)
print(f'A lista dos times em ordem alfabética é: {sorted(times)}')
print('...'*20)
print(f'Em qual posição está a Chapecoense: {times.index("Chapecoense")}')
