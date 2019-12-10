def norecursive(word):
    return word == word[::-1]


def norec2(word):
    czyjest = True
    dlg = len(word)
    for i in range(0, int(dlg / 2)):
        if czyjest:
            if word[i] != word[dlg - 1 - i]:
                czyjest = False
        else:
            break
    return czyjest


def recursive(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return recursive(word[1:-1])


a = str(input('Podaj slowo: '))

if norecursive(a):
    print('(bez rekurencji)Jest palindromem.')
else:
    print('(bez rekurencji)Nie jest palindromem.')

if norec2(a):
    print('(bez rekurencji2)Jest palindromem.')
else:
    print('(bez rekurencji2)Nie jest palindromem.')

if recursive(a):
    print('(rekurencja)Jest palindromem.')
else:
    print('(rekurencja)Nie jest palindromem.')
