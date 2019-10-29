A = int(input('Podaj A: '))
B = int(input('Podaj B: '))


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


print('Najwiekszy wspolny dzielnik:', nwd(A, B))
