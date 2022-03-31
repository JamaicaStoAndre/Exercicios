from math import sin, cos, radians, tan
angulo = float(input('Digite o ângulo que vc deseja: '))
seno = sin(radians(angulo))
print('O ângunlo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O valor do seno do ângulo {} é: {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O valor da tangente do ângulo {} é de {:.2f}'.format(angulo, tangente))

