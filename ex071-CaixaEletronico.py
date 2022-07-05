valor = float(input('Qual valor deseja sacar: '))
cedula50 = cedulas20 = resto50 = cedulas01 = resto20 = resto10 = cedulas10 = 0

resto = 0
if valor >= 50:
    print('Maior de 50')
    cedula50 = int(valor / 50)
    resto50 = valor % 50
    cedulas20 = resto50 % 20
    resto20 = resto50 / 20
    #cedulas10 = ()
    if resto50 >= 20 and resto50 < 50:
        cedulas20 = int(resto50 / 20)
        resto20 = int(resto50 / 20)
        if resto20 >= 10 or resto20 < 20:
            cedulas10 += 1

elif valor < 50 and valor >= 20:
    cedulas20 = int(valor / 20)
    resto = valor % 20
    print('Menor de 50, maior que 20')
elif valor < 20 and valor >= 10:
    resto = valor % 10
    print('Menor de 20, maior que 10')
else:
    resto = valor % 1
    print('Menor de 10, maior que 1')
print(f'Cedulas de 50: {cedula50}. Resto de 50:-- {resto50}')
print(f'Resto de 20: {resto20}. ')
print(f'Cedulas de 20: {cedulas20}')
print(f'Cedulas de 10: {cedulas10}')


