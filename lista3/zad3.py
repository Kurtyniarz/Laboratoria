suma = 0

n = int(input('Ile liczb chcesz dodac do sredniej: '))

for i in range(0,n):
    a = float(input('Podaj liczbę do średniej: '))
    suma += a

avg = suma/n

print('Srednia:', avg)