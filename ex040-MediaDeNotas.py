n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2
if media >= 5 and media < 7:
    print('As notas {:.1f} e {:.1f}, tem a média de: {:.1f} e você está em RECUPERAÇÂO!'.format(n1, n2, media))
elif media < 5:
    print('Com as notas {:.1f} e {:.1f}, você tem a média de: {:.1f}. Está REPROVADO'.format(n1, n2, media))
else:
    print('Com as notas {:.1f} e {:.1f}, você tem a média de: {:.1f}, você foi APROVADO'.format(n1, n2, media))
