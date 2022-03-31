from time import sleep
segundos = int(input('Digite a quantidade de segundos: '))
for c in range(segundos, -1, -1): #o primeiro -1 é pq o 0 é ignorado
    print(c)
    sleep(1)