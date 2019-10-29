silnia = 1

N = int(input('Podaj liczbe, ktora silnie chcesz obliczyc: '))

if N == 0:
    print('Silnia jest rowna:', silnia)
else:
    for i in range(1, (N + 1)):
        silnia *= i
    print('Silnia jest rowna:', silnia)
