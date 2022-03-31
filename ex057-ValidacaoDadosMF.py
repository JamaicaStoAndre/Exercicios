sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]#Fatia a string e pega soemtne o primeiro elemento
registro = 1
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor digite H ou M: ')).strip().upper()[0]
    registro +=1
print(f'Sexo {sexo} , registrado com sucesso!, {registro} registros. ')