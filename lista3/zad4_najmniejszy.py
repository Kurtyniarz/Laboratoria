A = int(input('Podaj liczbe a: '))
B = int(input('Podaj liczbe b: '))

min = 0
if A > B:
    min = A
elif B > A:
    min = B
else:
    min = A

czyznaleziono = False
nmwd = 0
for i in range(2, min+1):
    if czyznaleziono is True: break
    if A % i == 0 and B % i == 0:
        nmwd = i
        czyznaleziono = True

if czyznaleziono:
    print('Znaleziono najmniejszy wspolny dzielnik:', nmwd)
else:
    print('Nie znaleziono najmniejszego wspolnego dzielnia...')