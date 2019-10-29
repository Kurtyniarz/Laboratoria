def trojkat(bok):
    for i in range(0, bok):
        row = ''
        for n in range(0, i+1):
            if n == 0:
                row += '*'
            elif n != i:
                row += ' '
            elif n == i:
                if i == bok-1:
                    row = (i+1) * '*'
                else:
                    row += '*'
        print(row)

a = int(input('Podaj bok trojkata: '))
trojkat(a)