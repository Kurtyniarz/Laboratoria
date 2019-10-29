import math

print('Ogolna postac funkcji kwadratowej: Ax^2 + Bx + C')

A = float(input('Podaj wspolczynnik A: '))
B = float(input('Podaj wspolczynnik B: '))
C = float(input('Podaj wspolczynnik C: '))

delta = (B ** 2) - (4 * A * C)

if delta < 0:
    print('Brak rozwiazania.')
elif delta == 0:
    x1 = (-B)/(2 * A)
    print('Jest jedno rozwiazaine:', x1)
elif delta > 0:
    delta = math.sqrt(delta)
    x1 = (-B - delta) / (2 * A)
    x2 = (-B + delta) / (2 * A)
    print('Sa dwa rozwiazania: ' + str(x1) + ' i ' + str(x2))

